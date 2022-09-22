
from flask import jsonify
from flask import Blueprint

from flaskr.cp_mexico.models.estado_model import Estado
from flaskr.cp_mexico.models.municipio_model import Municipio
from flaskr.cp_mexico import estado_schema, estados_schema, municipios_schema

bp = Blueprint('cp_mexico', __name__, url_prefix='/api')

@bp.get('/estados')
def get_estados():
    all_estados = Estado.query.all()
    result = estados_schema.dump(all_estados)
    
    return jsonify(result)

@bp.get('/municipios')
def get_estados():
    all_municipios = Municipio.query.all()
    result = municipios_schema.dump(all_municipios)
    
    return jsonify(result)

@bp.get('/actualizacion-base')
def actualizar_base():
    pass