import requests
from datetime import date
import pandas as pd

# Função que realiza a captura de todos os dados, deve-se passar o tipo de dado e o número do estado 
def request_data(tipo, uf):
    if tipo == 'totalLeitos':      
        http = 'https://covid-insumos.saude.gov.br/paineis/insumos/graficos/uti.php?uf=' + uf + ''
    elif tipo == 'leitosAlocados':
        http = 'https://covid-insumos.saude.gov.br/paineis/insumos/graficos/graflocados.php?uf=' + uf + ''
    elif tipo == 'respiradores':
        http = 'https://covid-insumos.saude.gov.br/paineis/insumos/graficos/respiradores.php?uf=' + uf + ''
    elif tipo == 'leitosSUS':
        http = 'https://covid-insumos.saude.gov.br/paineis/insumos/graficos/uti_sus.php?uf=' + uf + ''
    elif tipo == 'leitosPrivados':
        http = 'https://covid-insumos.saude.gov.br/paineis/insumos/graficos/uti_n_sus.php?uf=' + uf + ''
    
    page = requests.get(http)
    data = page.text
    data = data[(data.find('data: [') + 7):]
    data = data[:data.find(',')]
    return data

# Lista com número dos estados
estados_num = ['11','12','13','14','15','16','17','21','22','23','24','25','26','27','28','29','21','31','32','33','35','50','51','52','53','41','42','43']

# Dicionário relacionando número do estado com sua unidade federativa 
dic_UF = {
    '11':'RO', '12':'AC', '13':'AM', '14':'RR', '15':'PA', '16':'AP', '17':'TO',
    '21':'MA', '22':'PI', '23':'CE', '24':'RN', '25':'PB', '26':'PE', '27':'AL', '28':'SE', '29':'BA',
    '31':'MG', '32':'ES', '33':'RJ', '35':'SP',
    '41':'PR', '42':'SC', '43':'RN',
    '50':'MS', '51':'MT', '52':'GO', '53':'DF'
}

ds = []

for x in estados_num:
    UF = dic_UF[x]
    Total_Leitos = request_data('totalLeitos', x)
    Leitos_Alocados = request_data('leitosAlocados', x)
    Respiradores = request_data('respiradores', x)
    Leitos_SUS = request_data('leitosSUS', x)
    Leitos_Privados = request_data('leitosPrivados', x)

    append = [UF, Leitos_Alocados, Respiradores, Total_Leitos, Leitos_SUS, Leitos_Privados]
    ds.append(append)

# Cria o dataframe
UTI_SUS = pd.DataFrame(data = ds, columns = ['UF', 'Leitos locados', 'Respiradores', 'Total de Leitos','Leitos SUS', 'Leitos Privados'])
print(UTI_SUS)
