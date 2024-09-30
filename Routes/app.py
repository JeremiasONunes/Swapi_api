from flask import Flask, jsonify
from models import db  # Importação do db

# Importações dos Blueprints
from Routes.character_routes import character_bp
from Routes.movie_routes import movie_bp
from Routes.planet_routes import planet_bp
from Routes.starship_routes import starship_bp
from Routes.species_routes import species_bp
from Routes.vehicle_routes import vehicle_bp
from Routes.favorite_routes import favorite_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Registro dos Blueprints
    app.register_blueprint(character_bp)
    app.register_blueprint(movie_bp)
    app.register_blueprint(planet_bp)
    app.register_blueprint(starship_bp)
    app.register_blueprint(species_bp)
    app.register_blueprint(vehicle_bp)
    app.register_blueprint(favorite_bp)

    return app

app = create_app()

# Rota principal
@app.route('/', methods=['GET'])
def home():
    endpoints = {}
    
    # Iterar sobre todos os endpoints registrados
    for rule in app.url_map.iter_rules():
        endpoints[rule.endpoint] = {
            "methods": list(rule.methods),
            "url": str(rule)
        }
    
    return jsonify({
        "message": "Bem-vindo à API SWAPI!",
        "endpoints": endpoints
    })

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
