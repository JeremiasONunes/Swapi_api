import pytest
from app import create_app, db  # Importando a função de criação do app e db
from flask import jsonify

@pytest.fixture
def client():
    # Cria uma aplicação Flask em modo de teste
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Usando um banco de dados em memória para os testes
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()  # Cria todas as tabelas

    yield app.test_client()  # Retorna um cliente de teste

    with app.app_context():
        db.drop_all()  # Limpa o banco de dados após os testes

def test_home(client):
    response = client.get('/')  # Faz uma requisição GET para a rota principal
    json_data = response.get_json()  # Obtém os dados da resposta em formato JSON

    # Verifica se a resposta contém a mensagem esperada
    assert response.status_code == 200
    assert json_data['message'] == 'Bem-vindo à API SWAPI!'
    assert 'endpoints' in json_data  # Verifica se a chave 'endpoints' está na resposta
