
from flaskr.cp_mexico.models.asentamiento_model import AsentamientoSchema
from flaskr.cp_mexico.models.estado_model import EstadoSchema
from flaskr.cp_mexico.models.municipio_model import MunicipioSchema


estado_schema = EstadoSchema()
estados_schema = EstadoSchema(many=True)
municipio_schema = MunicipioSchema()
municipios_schema = MunicipioSchema(many=True)
asentamiento_schema = AsentamientoSchema()
asentamientos_schema = AsentamientoSchema(many=True)