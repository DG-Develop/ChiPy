from flaskr.cp_mexico.models.asentamiento_model import Asentamiento
from flaskr.cp_mexico.models.estado_model import Estado
from flaskr.cp_mexico.models.municipio_model import Municipio

from flaskr.cp_mexico import estado_schema, estados_schema, municipios_schema, asentamientos_schema, municipio_schema, asentamiento_schema
from flaskr.scripts.insert_address import get_asentamientos_excel, get_ciudades_excel, get_estados_excel, get_municipios_excel

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
                estado_encontrado = Estado.query.filter_by(
                    nombre_estado=municipio_dict["estado"]).first()
                municipio = Municipio(
                    estado_encontrado.id_estado, municipio_dict["municipio"], municipio_dict["clave_municipio"])

                db.session.add(municipio)
                db.session.commit()
                db.session.refresh(municipio)
                municipios_creados.append(municipio_schema.dump(municipio))

        return municipios_creados

    def InsertarAsentamientos(self):
        asentamientos = get_asentamientos_excel()
        asentamientos_creados = []

        for asentamiento_dict in asentamientos:
            asentamiento_encontrado = Asentamiento.query.filter(
                Asentamiento.codigo_postal == asentamiento_dict["codigo_postal"],
                Asentamiento.nombre_asentamiento == asentamiento_dict["nombre_asentamiento"],
                Asentamiento.tipo_asentamiento == asentamiento_dict["tipo_asentamiento"],
                Asentamiento.clave_tipo_asentamiento == asentamiento_dict["clave_tipo_asentamiento"],
                Asentamiento.nombre_ciudad == asentamiento_dict["ciudad"],
                Asentamiento.clave_ciudad == asentamiento_dict["clave_ciudad"],
                Asentamiento.identificador_asentamiento == asentamiento_dict[
                    "identificador_asentamiento"],
                Asentamiento.descripcion_zona == asentamiento_dict["descripcion_zona"],
                Asentamiento.municipio.has(
                    nombre_municipio=asentamiento_dict["municipio"])
            ).first()

            if asentamiento_encontrado is None:
                municipio_encontrado = Municipio.query.filter(
                    Municipio.nombre_municipio == asentamiento_dict["municipio"],
                    Municipio.clave_municipio == asentamiento_dict["clave_municipio"],
                    Municipio.estado.has(
                        nombre_estado=asentamiento_dict["estado"])
                ).first()

                asentamiento = Asentamiento(municipio_encontrado.id_municipio, asentamiento_dict["codigo_postal"], asentamiento_dict["nombre_asentamiento"], asentamiento_dict["tipo_asentamiento"], asentamiento_dict["clave_tipo_asentamiento"], asentamiento_dict["ciudad"], asentamiento_dict["clave_ciudad"], asentamiento_dict["identificador_asentamiento"], asentamiento_dict["descripcion_zona"])
                
                db.session.add(asentamiento)
                db.session.commit()
                db.session.refresh(asentamiento)
                asentamientos_creados.append(asentamiento_schema.dump(asentamiento))
                
        return asentamientos_creados