from datetime import date
from flask import jsonify
from flaskr.contratos.models.contrato_model import Contrato
from flaskr.contratos import contrato_schema, contratos_schema, dependencia_contrato_scheama
from sqlalchemy import extract
from sqlalchemy.orm import contains_eager

from flaskr.contratos.models.dependencia_model import Dependencia


class ContratoRepository:

    def ObtenerContratos(self, folio=""):
        if folio != "":
            all_contratos = Contrato.query.filter_by(folio=folio)
        else:
            all_contratos = Contrato.query.all()

        result = contratos_schema.dump(all_contratos)

        return jsonify(result)

    def ObtenerTop5Contratos(self):
        pass

    def ObtenerCantidadContratosPorDependencia(self):
        # contratos = Contrato.query.filter(
        #     extract('year', Contrato.fecha_ini) == 2022)
        
        dependencias = Dependencia.query.join(Contrato).filter(
            extract('year', Contrato.fecha_ini) == 2022
        )

        # j = join(Contrato, Dependencia, Contrato.id_dependencia == Dependencia.id_dependencia)

        # stmt = select(Contrato).select_from(j)

        result = dependencia_contrato_scheama.dump(dependencias)

        return jsonify(result)
