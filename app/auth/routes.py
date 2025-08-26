#app/auth/routes.py
from flask import Blueprint, request, jsonify
from app.models import User
from app import db
from flask_jwt_extended import create_access_token

# define el blueprint
auth_bp = Blueprint('auth', __name__)

# Endpoints para registro y login
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Faltan datos'}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'El usuario ya existe'}), 409

    new_user = User(username=data['username'])
    new_user.set_password(data['password'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Usuario registrado exitosamente'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Faltan datos'}), 400

    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"role": user.role})
        
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Credenciales inválidas'}), 401
