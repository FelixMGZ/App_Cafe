from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

db = SQLAlchemy()

def create_app():

    # crea y configura la applicación
    app = Flask(__name__, instance_relative_config=True)

    # --- configuración JWT ---
    app.config['JWT_SECRET_KEY'] = 'super-secret'  # Cambia esto en producción

    print(f"DEBUG: JWT Secret Key cargada -> {app.config['JWT_SECRET_KEY']}")

    # --- configuración ---
    db_path = os.path.join(app.instance_path, 'cafes.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # --- inicializa la base de datos ---
    db.init_app(app)

    # --- inicializa JWT ---
    jwt = JWTManager(app)

    # --- registra los blueprints ---
    from .cafes.routes import cafes_bp
    from .toasters.routes import toasters_bp
    from .auth.routes import auth_bp

    app.register_blueprint(cafes_bp, url_prefix='/cafes')
    app.register_blueprint(toasters_bp, url_prefix='/toasters')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    return app 