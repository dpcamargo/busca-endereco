"""
Pesquisa de endereço a partir de um CEP usando a API https://viacep.com.br/
"""
import requests
import json

while True:
    cep = input('Insira um número de CEP: ')
    cep = cep.replace('-','')
    url = ''
    if(cep.isdigit() and len(cep) == 8):
        url = 'https://viacep.com.br/ws/' + cep + '/json/'
    else:
        print('Digite um CEP válido.')

    r = requests.get(url)
    if r.status_code == 200:
        dados = json.loads(r.text)
        print(dados.get('logradouro'))
    else:
        print('Request failed.')
    print()
