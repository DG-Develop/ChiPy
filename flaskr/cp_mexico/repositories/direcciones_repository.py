from flaskr.cp_mexico.models.asentamiento_model import Asentamiento
from flaskr.cp_mexico.models.ciudad_model import Ciudad
from flaskr.cp_mexico.models.estado_model import Estado
from flaskr.cp_mexico.models.municipio_model import Municipio

from flaskr.cp_mexico import estado_schema, estados_schema, municipios_schema, ciudades_schema, asentamientos_schema, municipio_schema
from flaskr.scripts.insert_address import get_asentamientos_excel, get_estados_excel, get_municipios_excel

from flaskr.cp_mexico.db.sql_server import db


class DireccionRepository:

    def InsertarEstados(self):
        estados = get_estados_excel()
        estados_creados = []

        for estado_dict in estados:
            estado_encontrado = Estado.query.filter_by(
                nombre_estado=estado_dict["estado"]).first()

            if estado_encontrado is None:
                estado = Estado(estado_dict['estado'],
                                estado_dict['clave_estado'])
                db.session.add(estado)
                db.session.commit()
                db.session.refresh(estado)
                estados_creados.append(estado_schema.dump(estado))

        return estados_creados

    def InsertarMuncipios(self):
        municipios = get_municipios_excel()
        municipios_creados = []

        for municipio_dict in municipios:
            municipio_encontrado = Municipio.query.filter(
                Municipio.nombre_municipio == municipio_dict["municipio"],
                Municipio.estado.has(nombre_estado=municipio_dict["estado"]),
                Municipio.clave_municipio == municipio_dict["clave_municipio"]
            ).first()
            
            if municipio_encontrado is None:
                estado_encontrado = Estado.query.filter_by(nombre_estado=municipio_dict["estado"]).first()
                municipio = Municipio(estado_encontrado.id_estado, municipio_dict["municipio"], municipio_dict["clave_municipio"])
                
                db.session.add(municipio)
                db.session.commit()
                db.session.refresh(municipio)
                municipios_creados.append(municipio_schema.dump(municipio))
                
        return municipios_creados
