import requests
import time
import string
import json
import pandas as pd

# Requisição do HTML da página
source = requests.get("http://plataforma.saude.gov.br/novocoronavirus/#COVID-19")
# Pega informação em texto do que foi requisitado
database_path = source.text
# Procura no HTML a posição inicial do dataset com a versão correta
start = database_path.find("http://plataforma.saude.gov.br/novocoronavirus/resources/scripts/database.js?v=")
# Delimita o final do dataset
end = start + 89
# Nome do dataset que será requisitado
database_path = database_path[start:end]

# Requisição do arquivo JSON
page = requests.get(database_path)
# Retorna o JSON em formato de texto
json_file = page.text
# Corta informações desnecessárias
json_file = json_file[13:]
# Transforma o JSON texto em um JSON 
json_file = json.loads(json_file)

# Filtra buscando somente informação referente ao Brasil
brazil_filter = json_file['brazil']

# Cria uma tuple vazio
dataset = []
# Realiza um for para preencher com as informações de data, estado, suspeitas, casos confirmados, descartados e óbitos
for x in brazil_filter:
    date = x['date']
    for y in x['values']:
        uid = y['uid']

        if('suspects' in y):
            suspects = y['suspects']
        else:
            suspects = 0

        if('cases' in y):
            cases = y['cases']
        else:
            cases = 0

        if('refuses' in y):
            refuses = y['refuses']
        else:
            refuses = 0

        if('deaths' in y):
            deaths = y['deaths']
        else:
            deaths = 0
        
        # Cria uma tuple auxiliar
        append = [date, uid, suspects, cases, refuses, deaths]
        # Insere a tuple auxiliar no dataset definitivo
        dataset.append(append)

# Transforma a tuple num Dataframe utilizando a biblioteca Pandas
df = pd.DataFrame(data = dataset, columns = ['Date', 'UID', 'Suspects', 'Cases', 'Refuses', 'Deaths'])
print(df)