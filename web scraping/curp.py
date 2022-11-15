import json
import zlib
import requests
from bs4 import BeautifulSoup


## Get website content
# print('Get Website content')
# url = 'https://www.gob.mx/curp/'
# content_data = requests.get(url, allow_redirects=True)

# print(content_data.text)

# soup = BeautifulSoup(content_data.content, 'html.parser')

# repcaptcha_token = soup.find(id='recaptcha-token')

# print(repcaptcha_token)

url_API = 'https://www.gob.mx/v1/renapoCURP/consulta'

payload = {
    'curp': "GOPD860817HCCMCV05",
    'ip': "127.0.0.1",
    'response': "03AEkXODBeU4fLevaVVO1TpFctHn6PVHOWruSJ0VffvqwLgyc2aWrhmRavJgB8vMEG-d6xQ3EVaHBk6lSu4uSVbhdM44M1qbOFB_qoTuLFctVEgz7wLI7UPGkmR2X5LNZ9rHclc_ad_ZR1jJpbw63Yfu2BFJ2wGJKWbz6v9UgopBSAlpaxo88IZkocPmKzMMhGNtDAefFdnFtI8p4kjO2icZkbMj8m9pd1Zl0jQKV0HzhB4kewBBitxJ1AquM4jveNGSUqleSxoBSWJ5_mufEyAu_Pot4dAb0h-n-iKUW0B3OUJ1XiF-V7MQCZwErkHavFYupd9YCHRA4NPzvfo679yawt6rbjNzmzqMnOlg0R9pfagtLRSdiJLLDTzayi9FV_Ni8PixJ5a6HPYWHGpe9QHlsk1EH9y2C9pEKaiF_ACSUL9nCabf8ce2B_5CEYv9n1AJ9QfbezLBG_4cX8gH4mD__KepruRhe7M8Koi4sqI2F7sTu3uYJl9iJywNkEvO7t0nrGf_Xy3u9OhKqsD2M9rcFDCCD598PguA",
    'tipoBusqueda': "curp"
}

# headers = {
#     'Content-type': 'application/json',
#     'Accept': 'application/json',
#     'Access-Control-Allow-Origin': '*',
#     'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept',
#     'X-Requested-With': None
# }

headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json'
}


# request_body = zlib.compress(json.dumps(payload).encode('utf-8'))

stringify_body = json.dumps(payload).encode('utf-8')

response = requests.post(url=url_API, json=payload, headers=headers)

print(response.content)
