from flask import jsonify
from flaskr.contratos.models.contrato_model import Contrato
from flaskr.contratos import contrato_schema, contratos_schema


class ContratoRepository:
    
    def ObtenerContratos(self, folio=""):
        if folio != "":
            all_contratos = Contrato.query.filter_by(folio=folio)
        else :
            all_contratos = Contrato.query.all()
            
        result = contratos_schema.dump(all_contratos)
        
        return jsonify(result)
    
    def ObtenerTop5Contratos(self):
        pass
    
    