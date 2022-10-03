from sqlalchemy import Column, Integer, String
from flaskr.cp_mexico.db.sql_server import db, ma

class Estado(db.Model):
    __tablename__ = 'Estados'
    __bind_key__ = 'cp'
    
    id_estado = Column(Integer, primary_key=True, nullable=False)
    nombre_estado = Column(Integer, nullable=False)
    clave_estado = Column(String(3), nullable=False)
    
    def __init__(self, nombre_estado, clave_estado):
        self.nombre_estado = nombre_estado
        self.clave_estado = clave_estado
    

class EstadoSchema(ma.Schema):
    class Meta:
        fields = ('id_estado', 'nombre_estado', 'clave_estado')