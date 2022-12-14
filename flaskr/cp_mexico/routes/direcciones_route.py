from flask import jsonify
from flask import Blueprint

from flaskr.cp_mexico.models.asentamiento_model import Asentamiento
from flaskr.cp_mexico.models.estado_model import Estado
from flaskr.cp_mexico.models.municipio_model import Municipio

from flaskr.cp_mexico import estados_schema, municipios_schema, asentamientos_schema
from flaskr.cp_mexico.repositories.direcciones_repository import DireccionRepository

bp = Blueprint('cp_mexico', __name__, url_prefix='/api')
direccion_repository = DireccionRepository()

@bp.get('/estados')
def get_estados():
    all_estados = Estado.query.all()
    result = estados_schema.dump(all_estados)
    
    return jsonify(result)

@bp.get('/municipios')
def get_municipios():
    all_municipios = Municipio.query.all()
    result = municipios_schema.dump(all_municipios)
    
    return jsonify(result)


@bp.get('/asentamientos')
def get_asentamientos():
    all_asentamientos = Asentamiento.query.all()
    result = asentamientos_schema.dump(all_asentamientos)
    
    return jsonify(result)

@bp.get('/actualizacion-base-estados')
def actualizar_base_estados():
    estados = direccion_repository.InsertarEstados()    
    return estados

@bp.get('/actualizacion-base-municipios')
def actualizar_base_municipios():
    municipios = direccion_repository.InsertarMuncipios()
    return municipios

@bp.get('/actualizacion-base-asentamientos')
def actualizar_base_asentamientos():
    asentamientos = direccion_repository.InsertarAsentamientos()
    return asentamientos