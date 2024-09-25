from flask import Flask
from models import db 

def create_app():
    app = Flask(__name__)

    # Configurações da aplicação
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Ajuste conforme necessário
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o banco de dados com a aplicação
    db.init_app(app)

    # Registra suas rotas
    from .character_routes import character_bp  # Importa o blueprint
    app.register_blueprint(character_bp)

    # Registre outros blueprints conforme necessário
    from .movie_routes import movie_bp
    app.register_blueprint(movie_bp)

    from .planet_routes import planet_bp
    app.register_blueprint(planet_bp)

    from .starship_routes import starship_bp
    app.register_blueprint(starship_bp)

    from .species_routes import species_bp
    app.register_blueprint(species_bp)

    from .vehicle_routes import vehicle_bp
    app.register_blueprint(vehicle_bp)

    from .favorite_routes import favorite_bp
    app.register_blueprint(favorite_bp)

    return app

# O padrão de execução do aplicativo deve ser feito em outro arquivo, como app.py
