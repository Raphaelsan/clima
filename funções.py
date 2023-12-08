import requests
import xmltodict
from json import dumps


def localizar(cidade, chave):

    codigo_pais = 'BR'
    codigo_cidade = ''

    codigo_SP = '01000-000'
    codigo_RJ = '20000-000'

    if cidade == 'RJ':
        codigo_cidade = codigo_RJ
    elif cidade == 'SP':
        codigo_cidade = codigo_SP

    api_url = f'https://api.openweathermap.org/geo/1.0/zip?zip={codigo_cidade},{codigo_pais}&appid={chave}'

    response = requests.get(api_url)

    dados = response.json()

    if response.status_code == 200:
        cidade = dados['name']
        latitude = dados['lat']
        longitude = dados['lon']
        pais = dados['country']
        return cidade, pais, latitude, longitude
    elif response.status_code == 429:
        print('Excedeu uso')
    elif response.status_code == 404:
        print('Nome de cidade, código postal ou ID da cidade errados')
    else:
        print(f'response: {response}')


def clima(chave, latitude, longitude):
    lang = 'pt_br'
    api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={chave}&lang={lang}'

    response = requests.get(api_url)
    dados = response.json()
    return dados
