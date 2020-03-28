import requests
from datetime import date
import json
import pandas as pd

#### FONTE DE DADOS: GLOBO

# Requisição do arquivo JSON
page = requests.get('https://especiais.g1.globo.com/bemestar/coronavirus/mapa-coronavirus/data/brazil-cases.json')
# Retorna o JSON em formato de texto
json_file = page.text
# Transforma a string em uma estrutura JSON 
json_file = json.loads(json_file)
data_filter = json_file['docs']

dataset = []

for x in data_filter:

    estado = x['state']
    cidade = x['city_name']
    data = x['date']
    casos_confirmados = x['cases']

    append = [data, cidade, estado, casos_confirmados]
    dataset.append(append)

Casos_no_Brasil = pd.DataFrame(data = dataset, columns = ['Data', 'Cidade', 'Estado', 'Casos confirmados'])

#### FONTE DE DADOS BING

# Requisição do arquivo JSON
page = requests.get('https://www.bing.com/covid/data?IG=')
# Retorna o JSON em formato de texto
json_file = page.text
# Transforma a string em uma estrutura JSON 
json_file = json.loads(json_file)
# Filtra buscando somente informação referente ao Brasil
data_filter = json_file['areas']
brazil_filter = [x for x in data_filter if x['id'] == 'brazil']

dataset = []

for x in brazil_filter:
    for y in x['areas']:

        estado = y['displayName']
        casos_confirmados = y['totalConfirmed']
        obitos = y['totalDeaths']
        casos_recuperados = y['totalRecovered']
    
        append = [estado, casos_confirmados, obitos, casos_recuperados]
        dataset.append(append)

Casos_por_Estado = pd.DataFrame(data = dataset, columns = ['Estado', 'Casos Confirmados', 'Óbitos', 'Casos recuperados'])

print(Casos_por_Estado)
print(Casos_no_Brasil)