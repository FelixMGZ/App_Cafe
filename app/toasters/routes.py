from flask import Blueprint, jsonify, request
from ..models import Toaster
from app import db
from flask_jwt_extended import jwt_required, get_jwt

# Creamos el blueprint para los toasters    
toasters_bp = Blueprint('toasters', __name__)

# Ruta para obtener todos los toasters
@toasters_bp.route('/', methods=['GET'])
def get_toasters():
    toasters = [toaster.to_dict() for toaster in Toaster.query.all()]
    return jsonify({"toasters": toasters, "result": len(toasters)}), 200

@toasters_bp.route('/<int:toaster_id>', methods=['GET'])
def get_toaster_id (toaster_id):
    toaster = Toaster.query.get_or_404(toaster_id)
    return jsonify(toaster.to_dict()), 200  


@toasters_bp.route('/', methods=['POST'])
def create_toaster():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'El nombre del toaster es requerido'}), 400

    if Toaster.query.filter_by(name=data['name']).first():
        return jsonify({'error': 'El nombre del toaster ya existe'}), 409

    new_toaster = Toaster(name=data['name'])
    db.session.add(new_toaster)
    db.session.commit()
    return jsonify(new_toaster.to_dict()), 201

@toasters_bp.route('/<int:toaster_id>', methods=['PUT'])
def update_toaster(toaster_id):
    toaster = Toaster.query.get_or_404(toaster_id)
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'El nombre del toaster es requerido'}), 400

    if Toaster.query.filter(Toaster.name == data['name'], Toaster.id != toaster_id).first():
        return jsonify({'error': 'El nombre del toaster ya existe'}), 409

    toaster.name = data['name']
    db.session.commit()
    return jsonify(toaster.to_dict()), 200

@toasters_bp.route('/<int:toaster_id>', methods=['DELETE'])
@jwt_required()
def delete_toaster(toaster_id):
    toaster = Toaster.query.get_or_404(toaster_id)
    db.session.delete(toaster)
    db.session.commit()
    return jsonify({'message': 'Toaster eliminado'}), 200

