from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.orm import registry, relationship

mapper_registry=registry()

Base = mapper_registry.generate_base()

class Contrato(Base):
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

