import requests
from datetime import date
import json
import pandas as pd
from bs4 import BeautifulSoup

# Requisição do arquivo JSON
page = requests.get('https://api.especiaisg1.globo/api/eventos/brasil/?format=json')
# Retorna o JSON em formato de texto
json_file = page.text
# Transforma a string em uma estrutura JSON 
json_file = json.loads(json_file)
data_filter = json_file['docs']

dataset = []

# Loop no arquivo JSON
for x in data_filter:
    estado = x['state']
    if 'city_name' in x:
        cidade = x['city_name']
    else:
        cidade = 'null'
    data = x['date']
    casos_confirmados = x['cases']

    append = [data, cidade, estado, casos_confirmados]
    dataset.append(append)

# Cria o dataframe 
Casos_no_Brasil = pd.DataFrame(data = dataset, columns = ['Data', 'Cidade', 'Estado', 'Casos confirmados'])
print(Casos_no_Brasil)