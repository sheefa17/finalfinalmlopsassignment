import os
import sys
import pytest

# Add the app directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app import app  # This will now work

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Health Risk Classifier" in response.data

def test_predict_endpoint(client):
    response = client.post("/predict", data={"age": "45", "cholesterol": "220"})
    assert response.status_code == 200
    assert b"Risk" in response.data
