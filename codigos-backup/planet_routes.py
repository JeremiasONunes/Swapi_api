from flask import Blueprint, jsonify, request
from models import db, Planet

# Criação do Blueprint
planet_bp = Blueprint('planets', __name__)

# Função auxiliar para salvar um novo registro
def save_record(model, data):
    new_record = model(**data)
    db.session.add(new_record)
    db.session.commit()
    return new_record

# Rota para listar todos os planetas
@planet_bp.route('/planetas', methods=['GET'])
def get_planetas():
    planetas_list = Planet.query.all()
    result = [
        {
            "id": p.id,
            "name": p.name,
            "rotation_period": p.rotation_period,
            "orbital_period": p.orbital_period,
            "diameter": p.diameter,
            "climate": p.climate,
            "gravity": p.gravity,
            "terrain": p.terrain,
            "surface_water": p.surface_water,
            "population": p.population
        } for p in planetas_list
    ]
    return jsonify(result)

# Rota para retornar um planeta específico pelo ID
@planet_bp.route('/planetas/<int:id>', methods=['GET'])
def get_planeta(id):
    p = Planet.query.get(id)
    if p:
        return jsonify({
            "id": p.id,
            "name": p.name,
            "rotation_period": p.rotation_period,
            "orbital_period": p.orbital_period,
            "diameter": p.diameter,
            "climate": p.climate,
            "gravity": p.gravity,
            "terrain": p.terrain,
            "surface_water": p.surface_water,
            "population": p.population
        })
    return jsonify({"error": "Planeta não encontrado"}), 404

# Rota para salvar um planeta no banco de dados
@planet_bp.route('/planetas', methods=['POST'])
def save_planeta():
    data = request.json
    new_planeta = save_record(Planet, data)
    return jsonify({"message": "Planeta salvo com sucesso!", "id": new_planeta.id}), 201

# Rota para deletar um planeta pelo ID
@planet_bp.route('/planetas/<int:id>/delete', methods=['DELETE'])
def delete_planeta(id):
    p = Planet.query.get(id)
    if p:
        db.session.delete(p)
        db.session.commit()
        return jsonify({"message": "Planeta deletado com sucesso!"})
    return jsonify({"error": "Planeta não encontrado"}), 404
