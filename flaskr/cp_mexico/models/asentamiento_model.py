from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flaskr.cp_mexico.db.sql_server import db, ma
from marshmallow import fields
from flaskr.cp_mexico.models.municipio_model import MunicipioSchema
from flaskr.cp_mexico.models.ciudad_model import CiudadSchema


class Asentamiento(db.Model):
    __tablename__ = 'Asentamientos'
    __bind_key__ = 'cp'
    
    id_asentamiento = Column(Integer, primary_key=True, nullable=False)
    id_municipio = Column(Integer, ForeignKey('Municipios.id_municipio'), nullable=False)
    id_ciudad = Column(Integer, ForeignKey('Ciudades.id_ciudad'), default=0)
    codigo_postal = Column(String(6), nullable=False)
    nombre_asentamiento = Column(String(400), nullable=False)
    tipo_asentamiento = Column(String(100), nullable=False)
    clave_tipo_asentamiento = Column(String(3), nullable=False)
    identificador_asentamiento = Column(String(4), nullable=False)
    descripcion_zona = Column(String(50), nullable=False)
    
    municipio = relationship("Municipio")
    ciudad = relationship("Ciudad")
    
    def __init__(self, id_municipio, id_ciudad, codigo_postal, nombre_asentamiento, tipo_asentamiento, clave_tipo_asentamiento, identificador_asentamiento, descripcion_zona):
        self.id_municipio = id_municipio
        self.id_ciudad = id_ciudad
        self.codigo_postal = codigo_postal
        self.nombre_asentamiento = nombre_asentamiento
        self.tipo_asentamiento = tipo_asentamiento
        self.clave_tipo_asentamiento = clave_tipo_asentamiento
        self.identificador_asentamiento = identificador_asentamiento
        self.descripcion_zona = descripcion_zona
    
class AsentamientoSchema(ma.Schema):
    municipio = fields.Nested(MunicipioSchema)
    ciudad = fields.Nested(CiudadSchema)
    class Meta:
        fields = ('id_asentamiento', 'id_municipio', 'id_ciudad', 'codigo_postal', 'nombre_asentamiento', 'tipo_asentamiento', 'clave_tipo_asentamiento', 'identificador_asentamiento', 'descripcion_zona', 'municipio', 'ciudad')