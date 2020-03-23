import requests
import time
import string
import json
import pandas as pd

# Requisição do arquivo JSON
page = requests.get('https://sigageomarketing.com.br/coronavirus/coronavirus.js')
# Retorna o JSON em formato de texto
json_file = page.text
# Corta informações desnecessárias
json_file = json_file[12:]
# Transforma a string em uma estrutura JSON 
json_file = json.loads(json_file)

data_filters = json_file['features']
# Cria um tuple vazio
dataset = []
# Realiza um laço para preencher com as informações de data, estado, suspeitas, casos confirmados, descartados e óbitos
for x in data_filters:

    uid = x['properties']['estado_geo']
    
    casossuspeitos = x['properties']['casossuspeitos']
    casosconfirmados = x['properties']['casosconfirmados']
    casosdescartados = x['properties']['casosdescartados']
    obitos = x['properties']['obitos']

    # Cria um tuple auxiliar
    append = [uid, casossuspeitos, casosconfirmados, casosdescartados, obitos]
    # Insere o tuple auxiliar no dataset definitivo
    dataset.append(append)


# Transforma o tuple num Dataframe utilizando a biblioteca Pandas
df = pd.DataFrame(data = dataset, columns = ['UID', 'Casos suspeitos', 'Casos confirmados', 'Casos descartados', 'Óbitos'])
print(df)

