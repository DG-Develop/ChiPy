import pandas as pd
import time
import base64
import os

# from sel import scrap_cfdi
import datetime
from descarga_masiva_xml.webservicerequest import WebServiceRequest


from cfdiclient import (
    Autenticacion,
    DescargaMasiva,
    Fiel,
    VerificaSolicitudDescarga
)

class SolicitaDescargaUUID(WebServiceRequest):

    xml_name = 'solicitadescarga.xml'
    soap_url = 'https://cfdidescargamasivasolicitud.clouda.sat.gob.mx/SolicitaDescargaService.svc'
    soap_action = 'http://DescargaMasivaTerceros.sat.gob.mx/ISolicitaDescargaService/SolicitaDescarga'
    solicitud_xpath = 's:Body/des:SolicitaDescarga/des:solicitud'
    result_xpath = 's:Body/SolicitaDescargaResponse/SolicitaDescargaResult'

    def solicitar_descarga(
        self, token, rfc_solicitante, fecha_inicial=None, fecha_final=None,
        rfc_emisor=None, rfc_receptor=None, tipo_solicitud='CFDI',
        tipo_comprobante=None, estado_comprobante=None, 
        rfc_a_cuenta_terceros=None, complemento=None, uuid=None
    ):

        arguments = {
            'RfcSolicitante': rfc_solicitante,
            'FechaFinal': fecha_final.strftime(self.DATE_TIME_FORMAT),
            'FechaInicial': fecha_inicial.strftime(self.DATE_TIME_FORMAT),
            'TipoSolicitud': tipo_solicitud,
            'TipoComprobante': tipo_comprobante,
            'EstadoComprobante': estado_comprobante,
            'RfcACuentaTerceros': rfc_a_cuenta_terceros,
            'Complemento': complemento,
            'Folio': uuid,
        }

        if rfc_emisor:
            arguments['RfcEmisor'] = rfc_emisor

        if rfc_receptor:
            arguments['RfcReceptores'] = [rfc_receptor]

        element_response = self.request(token, arguments)

        ret_val = {
            'id_solicitud': element_response.get('IdSolicitud'),
            'cod_estatus': element_response.get('CodEstatus'),
            'mensaje': element_response.get('Mensaje')
        }

        return ret_val


# RFC = "GEC950401659"
RFC = "GEC950401659"
FIEL_CER = "static/fiels/00001000000712142649.cer"
FIEL_KEY = "static/fiels/Claveprivada_FIEL_GEC950401659_20241220_093407.key"
FIEL_PAS = "MasterJez19361985"
# FIEL_PAS = "MasterJez19361985"
FECHA_INICIAL = datetime.date(2025, 2, 14)
FECHA_FINAL = datetime.date(2025, 2, 28)
PATH = "static/xmls/"
UUID="02456177-1151-41c4-9f90-deda21e4e518"

fiel_cer = open(FIEL_CER, "rb").read()
fiel_key = open(FIEL_KEY, "rb").read()

fiel = Fiel(fiel_cer, fiel_key, FIEL_PAS)

auth = Autenticacion(fiel)

token = auth.obtener_token()


# Solicito la descarga Por UUID
descarga = SolicitaDescargaUUID(fiel)

solicitud = descarga.solicitar_descarga(
    token=token,
    rfc_solicitante=RFC,
    fecha_inicial='',
    fecha_final='',
    tipo_solicitud='CFDI',
    uuid=UUID,
)

print(solicitud)

while True:

    token = auth.obtener_token()

    verificacion = VerificaSolicitudDescarga(fiel)

    verificacion = verificacion.verificar_descarga(token, RFC, solicitud['id_solicitud'])

    print('SOLICITUD:', verificacion)

    estado_solicitud = int(verificacion['estado_solicitud'])

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

        print('ERROR:', estado_solicitud)

        break

    else:
        # Si el estatus es 3 se trata de descargar los paquetes

        for paquete in verificacion['paquetes']:

            descarga = DescargaMasiva(fiel)

            descarga = descarga.descargar_paquete(token, RFC, paquete)

            print('PAQUETE: ', paquete)
            
            with open(PATH + '{}.zip'.format(paquete), 'wb') as fp:
                    fp.write(base64.b64decode(descarga['paquete_b64']))
                    # os.remove(PATH + '{}.xml'.format(UUID))

            # with open(PATH + '{}.xml'.format(paquete), 'wb') as xml:
            #     xml_file = base64.b64decode(descarga['paquete_b64'])
            #     xml.write(xml_file)
                
                
            # with open(PATH + '{}.xml'.format(paquete), 'wb') as xml:
            #     os.rename(PATH + '{}.xml'.format(paquete), UUID)
                
            # with open(PATH + '{}.xml'.format(paquete), 'rb') as xml:
            #     with open(PATH + '{}.zip'.format(UUID), 'wb') as fp:
            #         fp.write(xml)
            #         os.remove(PATH + '{}.xml'.format(UUID))

        break


# Verifico la solicitud de la descarga
# v_descarga = VerificaSolicitudDescarga(fiel)

# result = v_descarga.verificar_descarga(token, RFC, id_solicitud)

# print(result)


#Descarga
# descarga = DescargaMasiva(fiel)

# result = descarga.descargar_paquete(token, RFC, id_solicitud)

# print(result)


# {'estad

# Cargo una lista de dataframes por cada hoja en el archivo
# dataframes = pd.read_excel(
#     'static/excel/sIN IDENTIFICAR.xlsx',
#     sheet_name=None,
#     converters={'folio': str}
# )

# data, not_passed = scrap_cfdi('019f2a1e-09ed-4436-90ab-ea7d3d457f49',fiel_key, fiel_cer)
