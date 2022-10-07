from sqlalchemy import Column, Integer, String
from flaskr.cp_mexico.db.sql_server import db, ma

class Ciudad(db.Model):
    __tablename__ = 'Ciudades'
    __bind_key__ = 'cp'
    
    id_ciudad = Column(Integer, primary_key=True, nullable=False)
    nombre_ciudad = Column(String(200), nullable=False, default="")
    clave_ciudad = Column(String(3), nullable=False, default="")
    
    def __init__(self, nombre_ciudad, clave_ciudad):
        self.nombre_ciudad = nombre_ciudad
        self.clave_ciudad = clave_ciudad

class CiudadSchema(ma.Schema):
    class Meta: 
        fields = ('id_ciudad', 'nombre_ciudad', 'clave_ciudad')