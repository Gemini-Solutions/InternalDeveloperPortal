import json
import app

def test_create_employee():
    client = app.app.test_client()
    response = client.post('/employees', data=json.dumps({"name": "Alice", "position": "QA Engineer"}), content_type='application/json')
    assert response.status_code == 201

def test_get_employees():
    client = app.app.test_client()
    response = client.get('/employees')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert "employees" in data

def test_get_employee():
    client = app.app.test_client()
    response = client.get('/employees/1')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert "employee" in data

def test_get_nonexistent_employee():
    client = app.app.test_client()
    response = client.get('/employees/100')
    assert response.status_code == 404
    data = json.loads(response.get_data(as_text=True))
    assert "error" in data

def test_update_employee():
    client = app.app.test_client()
    response = client.put('/employees/1', data=json.dumps({"name": "Updated Name", "position": "Updated Position"}), content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert "employee" in data
    assert data["employee"]["name"] == "Updated Name"
    assert data["employee"]["position"] == "Updated Position"

def test_delete_employee():
    client = app.app.test_client()
    response = client.delete('/employees/1')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert "result" in data
