
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean, Text
from flaskr.contratos.db.sql_server import db, ma

class Dependencia(db.Model):
    __tablename__ = 'Dependencia'
    
    id_dependencia = Column(Integer, primary_key=True, nullable=False)
    nombre_dependencia = Column(String(200), nullable=False)
    fundamento_legal = Column(Text, nullable=False)
    direccion_dependencia = Column(String(500), nullable=False)
    creado = Column(DateTime, nullable=False)
    activo = Column(Boolean, nullable=False)
    genero = Column(String(1), nullable=False)
    part = Column(String(10), nullable=False)
    esDesconcentrado = Column(Boolean, nullable=False)
    rfc = Column(String(13), nullable=False)
    tipo_dependencia = Column(String(20), nullable=False)
    
    
    
class DependenciaSchema(ma.Schema):
    class Meta:
        fields= ('id_dependencia', 'nombre_dependencia', 'fundamento_legal', 'direccion_dependencia', 'creado', 'activo', 'genero', 'part', 'esDesconcentrado', 'rfc', 'tipo_dependencia')