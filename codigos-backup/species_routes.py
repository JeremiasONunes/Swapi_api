from flask import Blueprint, jsonify, request
from models import db, Species

# Criação do Blueprint
species_bp = Blueprint('species', __name__)

# Função auxiliar para salvar um novo registro
def save_record(model, data):
    new_record = model(**data)
    db.session.add(new_record)
    db.session.commit()
    return new_record

# Rota para listar todas as espécies
@species_bp.route('/especies', methods=['GET'])
def get_species():
    species_list = Species.query.all()
    result = [
        {
            "id": s.id,
            "name": s.name,
            "classification": s.classification,
            "designation": s.designation,
            "average_height": s.average_height,
            "skin_colors": s.skin_colors,
            "hair_colors": s.hair_colors,
            "eye_colors": s.eye_colors,
            "average_lifespan": s.average_lifespan,
            "language": s.language
        } for s in species_list
    ]
    return jsonify(result)

# Rota para retornar uma espécie específica pelo ID
@species_bp.route('/especies/<int:id>', methods=['GET'])
def get_species_by_id(id):
    s = Species.query.get(id)
    if s:
        return jsonify({
            "id": s.id,
            "name": s.name,
            "classification": s.classification,
            "designation": s.designation,
            "average_height": s.average_height,
            "skin_colors": s.skin_colors,
            "hair_colors": s.hair_colors,
            "eye_colors": s.eye_colors,
            "average_lifespan": s.average_lifespan,
            "language": s.language
        })
    return jsonify({"error": "Espécie não encontrada"}), 404

# Rota para salvar uma nova espécie no banco de dados
@species_bp.route('/especies', methods=['POST'])
def save_species():
    data = request.json
    new_species = save_record(Species, data)
    return jsonify({"message": "Espécie salva com sucesso!", "id": new_species.id}), 201

# Rota para deletar uma espécie pelo ID
@species_bp.route('/especies/<int:id>/delete', methods=['DELETE'])
def delete_species(id):
    s = Species.query.get(id)
    if s:
        db.session.delete(s)
        db.session.commit()
        return jsonify({"message": "Espécie deletada com sucesso!"})
    return jsonify({"error": "Espécie não encontrada"}), 404
