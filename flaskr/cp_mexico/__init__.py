
from flaskr.cp_mexico.models.estado_model import EstadoSchema
from flaskr.cp_mexico.models.municipio_model import MunicipioSchema


estado_schema = EstadoSchema()
estados_schema = EstadoSchema(many=True)
municipio_schema = MunicipioSchema(many=True)
municipios_schema = MunicipioSchema(many=True)