import uuid
import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime as DateTime
# url = "https://siacam.safin.campeche.gob.mx/app/Presupuesto/InstanciasSolicitudesPresupuestales/Consultar"

headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjQwQzIzM0Q4MTMxNTkwMThCQUZCNjNERTY4N0NBMjRGQ0UxN0I2MkQiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJRTUl6MkJNVmtCaTYtMlBlYUh5aVQ4NFh0aTAifQ.eyJuYmYiOjE3MzQwMzk2MDAsImV4cCI6MTczNDA0MDgwMCwiaXNzIjoiaHR0cHM6Ly9jdWVudGFzLnNhZmluLmNhbXBlY2hlLmdvYi5teCIsImF1ZCI6WyJodHRwczovL2N1ZW50YXMuc2FmaW4uY2FtcGVjaGUuZ29iLm14L3Jlc291cmNlcyIsInNpYWNhbV9zZXJ2aWRvciJdLCJjbGllbnRfaWQiOiI0MmJlZjFjMDcwNmQwOTIzOWE1Y2RkYTBiYjljMTdiMDI2NTUwNzEyODhjODZlYWIiLCJzdWIiOiJkZTQ4ZTgwMTYzZDY5ZWJiYzI2ZmUzOTU0OTc0OGZmYmY2YWYxOGU2ZGQyYjAzMDg4ZDAwODhhYzFlYmI1YmJiIiwiYXV0aF90aW1lIjoxNzM0MDM5NjAwLCJpZHAiOiJsb2NhbCIsInNjb3BlIjpbIm9wZW5pZCIsInByb2ZpbGUiLCJsYWJvcl9wcm9maWxlIiwiZW1haWwiLCJwaG9uZSIsInNpYWNhbV9zZXJ2aWRvciJdLCJhbXIiOlsicHdkIl19.Ivf7nez-j_3ekq853H58rl4EZKrKirrTYuEW8vbRQcOUgjTt9yj4tIR-ATepI849Zm0oX_EifbArgqZF4bZ1UrV6n_5fSvv-8h8td_41YTvIHV4yXAobnn5EU_jJXW41l_Rak6N6K-ouTabBhXHp8fTnv1w-F_7IwDlII5mZxdFF8rY9ykvAdpB-Tqp0wznMQGDSN7vsTLPagtHAoSgn_siuHRz3h0zfl1L3cpN58X1acnMSOv3x2lh3aW0S1ghc8-xsioIYVJnFusBMvOAcVz1tyJcF4mnlB_JBT2FyrtPkfBoe2HGE-DE0-g7ZVPTUevcvJdC6h9I_ZO_Ejln0TA", # Reemplaza con tu token válido
    "Cookie": "ASP.NET_SessionId=welticusqvnboihzzsemhtxs" #av3shrcgzblzzz2qta2ahvtq
}

data = {
    "tipoSolicitud": "18",
    "clasificacion": "28",
    "idSolicitud": "105",
    "estado": "4"
}

# response = requests.post(url, headers=headers, data=data)


url = "https://siacam.safin.campeche.gob.mx/app/Presupuesto/InstanciasSolicitudesPresupuestales/ObtenerPaginaGrilla?numeroPagina=1&paginasPorSeccion=10&setting=2&elementosPorPagina=200&tipoSolicitud=18&clasificacion=28&idSolicitud=105&estado=4&codigoBarras=&folio=&_=1734033409847"

response = requests.get(url, headers=headers)


# print("Status Code:", response.status_code)
# print("Response Body:", response.text)



html = response.text

# Analiza el HTML con BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Busca todos los enlaces que contengan 'idInstancia' en sus atributos 'href'
id_instancias = set()
for a in soup.find_all('a', href=True):
    href = a['href']
    if 'idInstancia' in href:
        # Extrae el valor de idInstancia usando una división en el parámetro
        parts = href.split("idInstancia=")
        if len(parts) > 1:
            id_instancia = parts[1].split("&")[0]  # Obtén el valor antes del siguiente parámetro
            id_instancias.add(id_instancia)

# Convierte el conjunto a lista para tener los valores únicos
id_instancias = list(id_instancias)

# Imprime el resultado
print("Número de idInstancias:", len(id_instancias))


url_download = "https://siacam.safin.campeche.gob.mx/app/Presupuesto/InstanciasSolicitudesPresupuestales/ObtenerReporteXML"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://siacam.safin.campeche.gob.mx/app/Inicio/Index",
}
cookies = {
    "ASP.NET_SessionId": "welticusqvnboihzzsemhtxs",  # Reemplaza con tu sesión válida
    "ts": "eeyJhbGciOiJSUzI1NiIsImtpZCI6IjQwQzIzM0Q4MTMxNTkwMThCQUZCNjNERTY4N0NBMjRGQ0UxN0I2MkQiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJRTUl6MkJNVmtCaTYtMlBlYUh5aVQ4NFh0aTAifQ.eyJuYmYiOjE3MzQwMzk2MDAsImV4cCI6MTczNDA0MDgwMCwiaXNzIjoiaHR0cHM6Ly9jdWVudGFzLnNhZmluLmNhbXBlY2hlLmdvYi5teCIsImF1ZCI6WyJodHRwczovL2N1ZW50YXMuc2FmaW4uY2FtcGVjaGUuZ29iLm14L3Jlc291cmNlcyIsInNpYWNhbV9zZXJ2aWRvciJdLCJjbGllbnRfaWQiOiI0MmJlZjFjMDcwNmQwOTIzOWE1Y2RkYTBiYjljMTdiMDI2NTUwNzEyODhjODZlYWIiLCJzdWIiOiJkZTQ4ZTgwMTYzZDY5ZWJiYzI2ZmUzOTU0OTc0OGZmYmY2YWYxOGU2ZGQyYjAzMDg4ZDAwODhhYzFlYmI1YmJiIiwiYXV0aF90aW1lIjoxNzM0MDM5NjAwLCJpZHAiOiJsb2NhbCIsInNjb3BlIjpbIm9wZW5pZCIsInByb2ZpbGUiLCJsYWJvcl9wcm9maWxlIiwiZW1haWwiLCJwaG9uZSIsInNpYWNhbV9zZXJ2aWRvciJdLCJhbXIiOlsicHdkIl19.Ivf7nez-j_3ekq853H58rl4EZKrKirrTYuEW8vbRQcOUgjTt9yj4tIR-ATepI849Zm0oX_EifbArgqZF4bZ1UrV6n_5fSvv-8h8td_41YTvIHV4yXAobnn5EU_jJXW41l_Rak6N6K-ouTabBhXHp8fTnv1w-F_7IwDlII5mZxdFF8rY9ykvAdpB-Tqp0wznMQGDSN7vsTLPagtHAoSgn_siuHRz3h0zfl1L3cpN58X1acnMSOv3x2lh3aW0S1ghc8-xsioIYVJnFusBMvOAcVz1tyJcF4mnlB_JBT2FyrtPkfBoe2HGE-DE0-g7ZVPTUevcvJdC6h9I_ZO_Ejln0TA", # Reemplaza con tu sesión válida
    "tok": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjQwQzIzM0Q4MTMxNTkwMThCQUZCNjNERTY4N0NBMjRGQ0UxN0I2MkQiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJRTUl6MkJNVmtCaTYtMlBlYUh5aVQ4NFh0aTAifQ.eyJuYmYiOjE3MzQwMzk2MDAsImV4cCI6MTczNDA0MDgwMCwiaXNzIjoiaHR0cHM6Ly9jdWVudGFzLnNhZmluLmNhbXBlY2hlLmdvYi5teCIsImF1ZCI6WyJodHRwczovL2N1ZW50YXMuc2FmaW4uY2FtcGVjaGUuZ29iLm14L3Jlc291cmNlcyIsInNpYWNhbV9zZXJ2aWRvciJdLCJjbGllbnRfaWQiOiI0MmJlZjFjMDcwNmQwOTIzOWE1Y2RkYTBiYjljMTdiMDI2NTUwNzEyODhjODZlYWIiLCJzdWIiOiJkZTQ4ZTgwMTYzZDY5ZWJiYzI2ZmUzOTU0OTc0OGZmYmY2YWYxOGU2ZGQyYjAzMDg4ZDAwODhhYzFlYmI1YmJiIiwiYXV0aF90aW1lIjoxNzM0MDM5NjAwLCJpZHAiOiJsb2NhbCIsInNjb3BlIjpbIm9wZW5pZCIsInByb2ZpbGUiLCJsYWJvcl9wcm9maWxlIiwiZW1haWwiLCJwaG9uZSIsInNpYWNhbV9zZXJ2aWRvciJdLCJhbXIiOlsicHdkIl19.Ivf7nez-j_3ekq853H58rl4EZKrKirrTYuEW8vbRQcOUgjTt9yj4tIR-ATepI849Zm0oX_EifbArgqZF4bZ1UrV6n_5fSvv-8h8td_41YTvIHV4yXAobnn5EU_jJXW41l_Rak6N6K-ouTabBhXHp8fTnv1w-F_7IwDlII5mZxdFF8rY9ykvAdpB-Tqp0wznMQGDSN7vsTLPagtHAoSgn_siuHRz3h0zfl1L3cpN58X1acnMSOv3x2lh3aW0S1ghc8-xsioIYVJnFusBMvOAcVz1tyJcF4mnlB_JBT2FyrtPkfBoe2HGE-DE0-g7ZVPTUevcvJdC6h9I_ZO_Ejln0TA" # Reemplaza con tu sesión válido
}


# Carpeta donde se guardarán los XML
output_folder = "xmlsiacam"
os.makedirs(output_folder, exist_ok=True)  # Crea la carpeta si no existe

def clean_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)


# Descargar cada archivo XML
for id_instancia in id_instancias:
    print(f"Descargando XML para idInstancia={id_instancia}...")
    response = requests.get(f"{url_download}?idInstancia={id_instancia}", headers=headers, cookies=cookies)
    
    if response.status_code == 200:
        # Extraer el nombre del archivo desde el encabezado Content-Disposition
        content_disposition = response.headers.get("content-disposition", "")
        filename = f"{id_instancia}.xml"  # Nombre predeterminado
        if "filename=" in content_disposition:
            filename = content_disposition.split("filename=")[1].strip()
            filename = clean_filename(filename)  # Limpiar el nombre del archivo
            # poner segundos en el filename
            index = uuid.uuid4()
            filename = str(index) +".xml"
            

        # Guardar el archivo XML
        file_path = os.path.join(output_folder, filename)
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Archivo guardado: {file_path}")
    else:
        print(f"Error {response.status_code} al descargar el archivo para idInstancia={id_instancia}.")

print("Descarga completada.")

