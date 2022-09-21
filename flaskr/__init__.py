# import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean

from contratos.db.sql_server import get_db

# from flaskr.contratos.db.sql_server import get_db, init_db, db, ma


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']  = get_db()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
# init_db(app)


class Contrato(db.Model):
    __tablename__ = 'Tbl_Contrato'
    
    id_contrato=Column(Integer, primary_key=True, nullable=False)
    folio=Column(String(200), nullable=False)
    puesto=Column(String(100), nullable=False)
    importe_sdo=Column(Float, nullable=False)
    fecha_ini=Column(DateTime, nullable=False)
    fecha_termino=Column(DateTime, nullable=False)
    fecha_nombramiento=Column(DateTime, nullable=False)
    tipo_contrato=Column(String(100))
    id_dependencia=Column(Integer, nullable=False)
    creado=Column(DateTime, nullable=False)
    id_empleado=Column(Integer, nullable=False)
    clave=Column(String(20))
    numero_oficio=Column(String(100))
    activo=Column(Boolean, nullable=False)
    escaneado=Column(Boolean, nullable=False)
    version_contrato=Column(String(100))
    fecha_cierre=Column(DateTime, nullable=False)
    
    def __init__(self, folio, puesto, importe_sdo, fecha_ini, fecha_termino, fecha_nombramiento, tipo_contrato, id_dependencia, creado, id_empleado, clave, numero_oficio, activo, escaneado, version_contrato, fecha_cierre):
        self.folio = folio
        self.puesto = puesto
        self.importe_sdo = importe_sdo
        self.fecha_ini = fecha_ini
        self.fecha_termino = fecha_termino
        self.fecha_nombramiento = fecha_nombramiento
        self.tipo_contrato = tipo_contrato
        self.id_dependencia = id_dependencia
        self.creado = creado
        self.id_empleado = id_empleado
        self.clave = clave
        self.numero_oficio = numero_oficio
        self.activo = activo
        self.escaneado = escaneado
        self.version_contrato = version_contrato
        self.fecha_cierre = fecha_cierre
        

class ContratoSchema(ma.Schema):
    class Meta:
        fields = ('folio', 'puesto', 'importe_sdo', 'fecha_ini', 'fecha_termino', 'fecha_nombramiento', 'tipo_contrato', 'id_dependencia', 'creado', 'id_empleado', 'clave', 'numero_oficio', 'activo', 'escaneado', 'version_contrato', 'fecha_cierre')
        

contrato_schema = ContratoSchema()
contratos_schema = ContratoSchema(many=True)

# @app.route('/api/contratos', methods=['GET'])

@app.route('/api/contratos', methods=['GET'])
def get_contratos():
    all_contratos = Contrato.query.all()
    result = contratos_schema.dump(all_contratos)
    
    return jsonify(result)

# if __name__ == "__main__":
#     app.run(debug=True)

# from flaskr.db import get_db, init_db

# def create_app(test_config=None):
#     app = Flask(__name__, instance_relative_config=True)
    
#     # app.config.from_mapping(
#     #     SECRET_KEY='dev',
#     #     SQLALCHEMY_DATABASE_URI=get_db()
#     # )
#     app.config['SQLALCHEMY_DATABASE_URI'] = get_db()
    
#     # if test_config is None:
#     #     app.config.from_pyfile('config.py', silent=True)
#     # else:
#     #     app.config.from_mapping(test_config)
    
#     # try:
#     #     os.makedirs(app.instance_path)
#     # except OSError:
#     #     pass
    
#     @app.get("/")
#     def hello_world():
#         return "<h1>Hola Mundo</h1>"
    
#     # from . import db
#     # db.init_app(app)
#     init_db(app)
    
#     from . import contratos
#     app.register_blueprint(contratos.bp)
    
#     # # Remuevo la session una vez que la apliación se pare
#     # @app.teardown_appcontext
#     # def shutdown_session(exception=None):
#     #     print('Apagando...')
#     #     db_session.remove()
        
#     return app