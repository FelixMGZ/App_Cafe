# tests/conftest.py

import pytest
from app import create_app, db # <-- 1. Importamos la factory y db

@pytest.fixture(scope='module')
def test_app():
    """Crea y configura una nueva instancia de la app para cada módulo de pruebas."""
    # 2. Creamos la app usando la factory
    app = create_app()
    
    app.config.update({
        "TESTING": True,
        # Usamos una base de datos en memoria para las pruebas
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })

    with app.app_context():
        db.create_all()
        yield app  # Devolvemos la app completa
        db.drop_all()

@pytest.fixture()
def test_client(test_app):
    """Crea un cliente de pruebas para nuestra app."""
    return test_app.test_client()