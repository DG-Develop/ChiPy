from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flaskr.cp_mexico.db.sql_server import db, ma

class Municipio(db.Model):
    __tablename__ = 'Municipios'
    __bind_key__ = 'cp'
    
    id_municipio = Column(Integer, primary_key=True, nullable=False)
    id_estado = Column(Integer, ForeignKey('Estados.id_estado'), nullable=False)
    nombre_municipio = Column(String(100), nullable=False)
    clave_municipio = Column(String(3), nullable=False)
    
    estado = relationship("Estado")
    
    def __init__(self, id_estado, nombre_municipio, clave_municipio):
        self.id_estado = id_estado
        self.nombre_municipio = nombre_municipio
        self.clave_municipio = clave_municipio
    
class MunicipioSchema(ma.Schema):
    class Meta:
        fields = ('id_municipio', 'id_estado', 'nombre_municipio', 'clave_municipio', 'estado')