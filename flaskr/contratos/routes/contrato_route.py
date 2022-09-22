
from flask import jsonify
from flask import Blueprint

from flaskr.contratos.models.contrato_model import Contrato
from flaskr.contratos import contrato_schema, contratos_schema

bp = Blueprint('contratos', __name__, url_prefix='/api')

@bp.get('/contratos')
def get_contratos():
    all_contratos = Contrato.query.all()
    result = contratos_schema.dump(all_contratos)
    
    return jsonify(result)