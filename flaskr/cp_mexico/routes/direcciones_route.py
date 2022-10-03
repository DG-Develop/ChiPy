from flask import jsonify
from flask import Blueprint

from flaskr.cp_mexico.models.asentamiento_model import Asentamiento
from flaskr.cp_mexico.models.ciudad_model import Ciudad
from flaskr.cp_mexico.models.estado_model import Estado
from flaskr.cp_mexico.models.municipio_model import Municipio

from flaskr.cp_mexico import estado_schema, estados_schema, municipios_schema, ciudades_schema, asentamientos_schema
from flaskr.scripts.insert_address import get_asentamientos_excel, get_estados_excel, get_municipios_excel

from flaskr.cp_mexico.db.sql_server import db

bp = Blueprint('cp_mexico', __name__, url_prefix='/api')

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

@bp.get('/ciudades')
def get_ciudades():
    all_ciudades = Ciudad.query.all()
    result = ciudades_schema.dump(all_ciudades)
    
    return jsonify(result)

@bp.get('/asentamientos')
def get_asentamientos():
    all_asentamientos = Asentamiento.query.all()
    result = asentamientos_schema.dump(all_asentamientos)
    
    return jsonify(result)

@bp.get('/actualizacion-base')
def actualizar_base():
    estados = get_estados_excel()
    estados_creados = []
    
    for estado_dict in estados:
        estado_encontrado = Estado.query.filter_by(nombre_estado=estado_dict["estado"]).first()
        
        if estado_encontrado is None:
            estado = Estado(estado_dict['estado'], estado_dict['clave_estado'])
            db.session.add(estado)
            db.session.commit()
            db.session.refresh(estado)
            estados_creados.append(estado_schema.dump(estado))
            
    # db.session.bulk_save_objects()
    
    # municipios = get_municipios_excel()
    # ciudades = get_estados_excel()
    # asentamientos = get_asentamientos_excel()
    
    return estados_creados