from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from flaskr.contratos.db.sql_server import db, ma
from marshmallow import fields
from flaskr.contratos.models.dependencia_model import DependenciaSchema

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
    id_dependencia=Column(Integer, ForeignKey('Dependencia.id_dependencia'), nullable=False)
    creado=Column(DateTime, nullable=False)
    id_empleado=Column(Integer, nullable=False)
    clave=Column(String(20))
    numero_oficio=Column(String(100))
    activo=Column(Boolean, nullable=False)
    escaneado=Column(Boolean, nullable=False)
    version_contrato=Column(String(100))
    fecha_cierre=Column(DateTime, nullable=False)
    
    dependencia = relationship("Dependencia")
    
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
    dependencia = fields.Nested(DependenciaSchema)
    class Meta:
        fields = ('folio', 'puesto', 'importe_sdo', 'fecha_ini', 'fecha_termino', 'fecha_nombramiento', 'tipo_contrato', 'id_dependencia', 'creado', 'id_empleado', 'clave', 'numero_oficio', 'activo', 'escaneado', 'version_contrato', 'fecha_cierre', 'dependencia')