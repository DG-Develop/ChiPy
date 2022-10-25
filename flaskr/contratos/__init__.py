
from flaskr.contratos.models.contrato_model import ContratoSchema, ContratoDepencendiaSchema
from flaskr.contratos.models.dependencia_model import DependenciaNombreSchema


contrato_schema = ContratoSchema()
contratos_schema = ContratoSchema(many=True)
dependencia_contrato_scheama = DependenciaNombreSchema(many=True)
