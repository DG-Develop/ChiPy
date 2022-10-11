import requests
import shutil
from bs4 import BeautifulSoup

# Web Scraping
base_url = 'https://www.correosdemexico.gob.mx'
url = 'https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx'

content_data = requests.get(url, allow_redirects=True)

soup = BeautifulSoup(content_data.content, 'html.parser')

view_state = soup.find(id='__VIEWSTATE')
event_validation = soup.find(id='__EVENTVALIDATION')

params = {
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


# file_zip = requests.post(url,json=params, stream=True, allow_redirects=True)


# print(file_zip.headers)

# with open('CPdescargaxls.zip', 'wb') as out_file:
#     shutil.copyfile(file_zip.raw, out_file)