from app.controllers.number_controller import number_bp
from flask import Flask

def test_classify_number_api():
    app = Flask(__name__)
    app.register_blueprint(number_bp)
    client = app.test_client()

    response = client.get('/api/classify-number?number=371')
    assert response.status_code == 200
    assert b"armstrong" in response.data