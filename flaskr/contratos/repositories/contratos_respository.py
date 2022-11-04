from flask import jsonify
from flaskr.contratos.models.contrato_model import Contrato
from flaskr.contratos import contratos_schema, dependencia_contrato_scheama
from sqlalchemy import extract
import matplotlib.pyplot as plt
import numpy as np

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
        dependencias = Dependencia.query.join(Contrato).filter(
            extract('year', Contrato.fecha_ini) == 2022
        )

        lista_dependencia = dependencia_contrato_scheama.dump(dependencias)
        
        lista_dependencia.sort(key=lambda x: x['count'], reverse=True)
        
        # make data:
        # names = [d['nombre_dependencia'][0:3] for d in lista_dependencia]
        # values = [d['count'] for d in lista_dependencia]
        
        # plot
        # fig, ax = plt.subplots()

        # ax.bar(names, values, width=1, edgecolor="white", linewidth=0.7)

        # ax.set(xlim=(0, len(lista_dependencia)), xticks=np.arange(0, len(lista_dependencia)),
        #     ylim=(0, 200), yticks=np.arange(1, 200))

        # plt.show()
        
        return jsonify(lista_dependencia)
