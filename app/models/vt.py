import requests
import json
import config

# Crie o arquivo config.py e adicione a chave da API
# Exemplo API_KEY_VT = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
API_KEY_VT = config.API_KEY_VT

def scan_url(urlscan):

    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': API_KEY_VT, 'resource': urlscan}
    response = requests.get(url, params=params)

    data = json.loads(response.text)
    print(data)

    if data['response_code'] == 0: # url não encontrada no database do VT
        resposta = False
    else:
        resposta = True if data['positives'] > 0 else False
    return resposta