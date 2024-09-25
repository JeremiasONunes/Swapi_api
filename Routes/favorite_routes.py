from flask import Blueprint, jsonify, request
from models import db, Favorite

# Criação do Blueprint
favorite_bp = Blueprint('favorite', __name__)

# Função auxiliar para salvar um novo registro
def save_record(model, data):
    new_record = model(**data)
    db.session.add(new_record)
    db.session.commit()
    return new_record

# Rota para salvar um favorito no banco de dados
@favorite_bp.route('/favoritos', methods=['POST'])
def save_favorite():
    data = request.json
    new_favorite = save_record(Favorite, data)
    return jsonify({"message": "Favorito salvo com sucesso!", "id": new_favorite.id}), 201

# Rota para retornar todos os favoritos
@favorite_bp.route('/favoritos', methods=['GET'])
def get_favorites():
    favorites_list = Favorite.query.all()
    result = [
        {
            "id": f.id,
            "character_name": f.character_name,
            "birth_year": f.birth_year,
            "movie_name": f.movie_name,
            "starship_name": f.starship_name,
            "starship_model": f.starship_model,
            "vehicle_name": f.vehicle_name,
            "vehicle_model": f.vehicle_model,
            "species_homeworld": f.species_homeworld,
            "species_language": f.species_language,
            "planet_name": f.planet_name,
            "planet_population": f.planet_population,
            "student_name1": f.student_name1,
            "registration1": f.registration1,
            "student_name2": f.student_name2,
            "registration2": f.registration2,
            "course": f.course,
            "university": f.university,
            "period": f.period
        } for f in favorites_list
    ]
    return jsonify(result)

# Rota para deletar um favorito pelo ID
@favorite_bp.route('/favoritos/<int:id>/delete', methods=['DELETE'])
def delete_favorite(id):
    f = Favorite.query.get(id)
    if f:
        db.session.delete(f)
        db.session.commit()
        return jsonify({"message": "Favorito deletado com sucesso!"})
    return jsonify({"error": "Favorito não encontrado"}), 404
