from os import remove
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# Web Scraping

## Get website content
print('Get Website content')
url = 'https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx'
content_data = requests.get(url, allow_redirects=True)
soup = BeautifulSoup(content_data.content, 'html.parser')

view_state = soup.find(id='__VIEWSTATE')
event_validation = soup.find(id='__EVENTVALIDATION')

## Generate de data to form request 
print('Generate data to form request')
payload = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__VIEWSTATE': view_state['value'],
    '__VIEWSTATEGENERATOR': 'BE1A6D2E',
    '__EVENTVALIDATION': event_validation['value'],
    'cboEdo': '00',
    'rblTipo': 'xls',
    'btnDescarga.x': '39',
    'btnDescarga.y': '5'
}

## Downloading postal codes from SEPOMEX
print('Downloading postal codes from SEPOMEX')
response = requests.post(url=url, data=payload)

zip_path = 'static/excel/CPdescargaxls.zip'

## Writing zip
print('Writing Zip')
open(zip_path, 'wb').write(response.content)

## Extracting zip
print('Extracting Zip')
with ZipFile(zip_path, 'r') as zipObj:
    zipObj.extractall(path='static/excel')

## Remove zip
print('Remove zip')
remove(zip_path)