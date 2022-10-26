
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from flaskr.contratos.db.sql_server import db, ma
from marshmallow import fields

# from flaskr.contratos.models.contrato_model import ContratoDepencendiaSchema

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

    contratos = relationship("Contrato", back_populates='dependencia')

class DependenciaSchema(ma.Schema):
    class Meta:
        fields= ('id_dependencia', 'nombre_dependencia', 'fundamento_legal', 'direccion_dependencia', 'creado', 'activo', 'genero', 'part', 'esDesconcentrado', 'rfc', 'tipo_dependencia')

class DependenciaNombreSchema(ma.Schema):
    contratos = fields.Nested('ContratoDepencendiaSchema', many=True, only=['count'])
    count = fields.Function(lambda obj: len(obj.contratos))
    class Meta:
        fields= ('nombre_dependencia', 'count')