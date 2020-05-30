import requests
from datetime import date
import pandas as pd

# Fonte: Labs Wesley Costa
# Requisição do arquivo CSV
page = requests.get('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities-time.csv')
# Retorna o JSON em formato de texto
csv_file = page.text

# Cria o dataframe
coronavirus = pd.DataFrame([x.split(',') for x in csv_file.split('\n')])
print(coronavirus)
