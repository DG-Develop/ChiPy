from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flaskr.cp_mexico.db.sql_server import db, ma

class Ciudad(db.Model):
    __tablename__ = 'Ciudades'
    __bind_key__ = 'cp'
    
    id_ciudad = Column(Integer, primary_key=True, nullable=False)
    clave_ciudad = Column(String(3), nullable=False)
    
    

class CiudadSchema(ma.Schema):
    class Meta: 
        fields = ('id_ciudad', 'clave_ciudad')