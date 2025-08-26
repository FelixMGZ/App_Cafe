# tests/test_toasters.py

# Asegúrate de que los imports coincidan con tu estructura (app, no project)
from app.models import Toaster 

def test_get_toasters(test_client):
    """
    Prueba que el endpoint GET /toasters/ funciona en un estado vacío.
    """
    response = test_client.get('/toasters/')
    assert response.status_code == 200
    json_data = response.get_json()
    
    # Asumimos que tu endpoint GET devuelve una estructura como esta.
    # Si devuelve solo una lista vacía, la aserción sería: assert json_data == []
    assert json_data == {'toasters': [], 'result': 0}

def test_add_toaster(test_client):
    """
    Prueba que se puede agregar un nuevo tostador vía POST a /toasters/
    """
    toaster_data = { "name": "Test Toaster" }
    response = test_client.post('/toasters/', json=toaster_data)
    assert response.status_code == 201

    json_data = response.get_json()
    assert json_data['name'] == 'Test Toaster'
    assert 'id' in json_data

    toaster_in_db = Toaster.query.filter_by(name='Test Toaster').first()
    assert toaster_in_db is not None