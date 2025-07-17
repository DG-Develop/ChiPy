import time
from cfdiclient import VerificaSolicitudDescarga, Fiel

# —————————————————————————————————————————————
# Parámetros que ya tienes guardados
RFC = "GEC950401659"
FIEL_CER = "static/fiels/00001000000712142649.cer"
FIEL_KEY = "static/fiels/Claveprivada_FIEL_GEC950401659_20241220_093407.key"
FIEL_PAS = "MasterJez19361985"
id_solicitud = '6324db5c-f8c9-4a9e-b11d-83791664255e'
token = 'eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE3NTI2OTUyODIsImV4cCI6MTc1MjY5NTg4MiwiaWF0IjoxNzUyNjk1MjgyLCJpc3MiOiJMb2FkU29saWNpdHVkRGVjYXJnYU1hc2l2YVRlcmNlcm9zIiwiYWN0b3J0IjoiMzAzMDMwMzAzMTMwMzAzMDMwMzAzMDM3MzEzMjMxMzQzMjM2MzQzOSJ9.mdJs7y8yjur50f25wUIsNHvV-MObzpoFIKygWfoZ5YM%26wrap_subject%3d3030303031303030303030373132313432363439'

fiel_cer = open(FIEL_CER, "rb").read()
fiel_key = open(FIEL_KEY, "rb").read()

fiel = Fiel(fiel_cer, fiel_key, FIEL_PAS) # o ya instanciado antes
# —————————————————————————————————————————————

# Crea el cliente de verificación
verificador = VerificaSolicitudDescarga(fiel)

while True:
    try:
        resp = verificador.verificar_descarga(token, RFC, id_solicitud)
        estado = int(resp['estado_solicitud'])
        print(f"Estado {estado} — {resp.get('mensaje', '')}")

        if estado in (1, 2):
            # Aceptada o en proceso: esperamos y volvemos a consultar
            time.sleep(60)
            continue

        if estado == 3:
            # Terminada: ya hay paquetes listos
            print("✅ Solicitud terminada. Paquetes disponibles:")
            for pkg in resp['paquetes']:
                print("   •", pkg)
        else:
            # 4=Error, 5=Rechazada, 6=Vencida
            print("⚠️ Solicitud finalizada con estado no satisfactorio:", estado)
        break

    except Exception as err:
        print("Error al verificar estado:", err)
        # Esperamos un poco antes de reintentar
        time.sleep(30)
