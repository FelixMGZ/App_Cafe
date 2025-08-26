from flask import Blueprint, jsonify, request
from ..models import Cafe, Toaster
from .. import db

cafes_bp =Blueprint('cafes', __name__)

@cafes_bp.route('/', methods=['GET'])
def get_cafes():
    cafes = [cafe.to_dict() for cafe in Cafe.query.all()]
    return jsonify({"cafes": cafes, "result": len(cafes)}), 200

@cafes_bp.route('/<int:cafe_id>', methods=['GET'])
def get_cafe_id(cafe_id):
    cafe = Cafe.query.get_or_404(cafe_id)
    return jsonify(cafe.to_dict()), 200

@cafes_bp.route('/', methods=['POST'])
def create_cafe():
    data = request.get_json()
    required_fields = ['name', 'price', 'toaster_id']
    if not all (field in data for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos'}), 400
    
    toaster = Toaster.query.get(data['toaster_id'])
    if not toaster:
        return jsonify({'error': 'El toaster especificado no existe'}), 404

    new_cafe = Cafe(name=data['name'], price=data['price'], description=data.get('description'), toaster_id=data['toaster_id'])
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(new_cafe.to_dict()), 201

@cafes_bp.route('/<int:cafe_id>', methods=['PUT'])
def update_cafe(cafe_id):
    cafe = Cafe.query.get_or_404(cafe_id)
    data = request.get_json()
    if 'name' in data:
        cafe.name = data['name']
    if 'price' in data:
        cafe.price = data['price']
    if 'description' in data:
        cafe.description = data['description']
    if 'toaster_id' in data:
        toaster = Toaster.query.get(data['toaster_id'])
        if not toaster:
            return jsonify({'error': 'El toaster especificado no existe'}), 404
        cafe.toaster_id = data['toaster_id']
    
    db.session.commit()
    return jsonify(cafe.to_dict()), 200

@cafes_bp.route('/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    cafe = Cafe.query.get_or_404(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return jsonify({'message': 'Café eliminado'}), 200
