
from flask import request
from flask import Blueprint
from flaskr.contratos.repositories.contratos_respository import ContratoRepository

bp = Blueprint('contratos', __name__, url_prefix='/api')

contrato_repository = ContratoRepository()

@bp.get('/contratos')
def get_contratos():
    folio = request.args['folio']
    contratos = contrato_repository.ObtenerContratos(folio=folio)
    
    return contratos

@bp.get('/contratos/dependencia-cantidad')
def obtener_contratos_por_cantidad_dependencia():
    contratos = contrato_repository.ObtenerCantidadContratosPorDependencia()
    
    return contratos