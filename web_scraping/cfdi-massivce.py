import base64
import datetime
import os
import time

from cfdiclient import Autenticacion, DescargaMasiva, Fiel, VerificaSolicitudDescarga

from descarga_emisor_masiva_xml.webservicerequest import WebServiceRequest


class SolicitaDescargaEmitidos(WebServiceRequest):
    xml_name        = 'solicitadescargaemitidos.xml'
    soap_url        = 'https://cfdidescargamasivasolicitud.clouda.sat.gob.mx/SolicitaDescargaService.svc'
    soap_action     = 'http://DescargaMasivaTerceros.sat.gob.mx/ISolicitaDescargaService/SolicitaDescargaEmitidos'
    solicitud_xpath = 's:Body/des:SolicitaDescargaEmitidos/des:solicitud'
    result_xpath    = 's:Body/SolicitaDescargaEmitidosResponse/SolicitaDescargaEmitidosResult'

    def solicitar_descarga(
        self,
        token,
        rfc_emisor,
        fecha_inicial,
        fecha_final,
        rfc_solicitante=None,
        tipo_solicitud="CFDI",
        tipo_comprobante=None,
        estado_comprobante=None,
    ):
        args = {
            "RfcEmisor": rfc_emisor,
            "RfcSolicitante": rfc_solicitante,
            "FechaInicial": fecha_inicial.strftime(self.DATE_TIME_FORMAT),
            "FechaFinal": fecha_final.strftime(self.DATE_TIME_FORMAT),
            "TipoSolicitud": tipo_solicitud,
            "TipoComprobante": tipo_comprobante,
            "EstadoComprobante": estado_comprobante,
        }
        # elimina claves None para no enviar atributos vacíos
        args = {k: v for k, v in args.items() if v is not None}

        element = self.request(token, args)
        return {
            "id_solicitud": element.get("IdSolicitud"),
            "cod_estatus": element.get("CodEstatus"),
            "mensaje": element.get("Mensaje"),
        }


RFC = "GEC950401659"
FIEL_CER = "static/fiels/00001000000712142649.cer"
FIEL_KEY = "static/fiels/Claveprivada_FIEL_GEC950401659_20241220_093407.key"
FIEL_PAS = "MasterJez19361985"
FECHA_INICIAL = datetime.date(2025, 2, 14)
FECHA_FINAL = datetime.date(2025, 3, 13)
PATH = "static/xmls/"

fiel_cer = open(FIEL_CER, "rb").read()
fiel_key = open(FIEL_KEY, "rb").read()

fiel = Fiel(fiel_cer, fiel_key, FIEL_PAS)

auth = Autenticacion(fiel)

token = auth.obtener_token()

print("TOKEN: ", token)

descarga = SolicitaDescargaEmitidos(fiel)

# EMITIDOS
solicitud = descarga.solicitar_descarga(
    token=token,
    rfc_emisor=RFC,
    fecha_inicial=FECHA_INICIAL,
    fecha_final=FECHA_FINAL,
    rfc_solicitante=RFC,  # opcional
    tipo_solicitud="CFDI",
)

# RECIBIDOS
# solicitud = descarga.solicitar_descarga(
#     token, RFC, FECHA_INICIAL, FECHA_FINAL, rfc_receptor=RFC, tipo_solicitud='CFDI'
# )


# token = auth.obtener_token()

# print("TOKEN: ", token)



print("SOLICITUD:", solicitud)

while True:

    try:
        token = auth.obtener_token()
        print("TOKEN:", token)
    except:
        print("⏱ Timeout obteniendo token, reintentando en 30 s…")
        time.sleep(30)
        continue

    verificacion = VerificaSolicitudDescarga(fiel)
    verificacion = verificacion.verificar_descarga(
        token, RFC, solicitud["id_solicitud"]
    )

    print("SOLICITUD:", verificacion)

    estado_solicitud = int(verificacion["estado_solicitud"])

    # 0, Token invalido.
    # 1, Aceptada
    # 2, En proceso
    # 3, Terminada
    # 4, Error
    # 5, Rechazada
    # 6, Vencida

    if estado_solicitud <= 2:

        # Si el estado de solicitud esta Aceptado o en proceso el programa espera
        # 60 segundos y vuelve a tratar de verificar
        time.sleep(60)

        continue

    elif estado_solicitud >= 4:

        print("ERROR:", estado_solicitud)

        break

    else:
        # Si el estatus es 3 se trata de descargar los paquetes

        for paquete in verificacion["paquetes"]:

            descarga = DescargaMasiva(fiel)

            descarga = descarga.descargar_paquete(token, RFC, paquete)

            print("PAQUETE: ", paquete)

            with open(PATH + "{}.zip".format(paquete), "wb") as fp:

                fp.write(base64.b64decode(descarga["paquete_b64"]))

        break
