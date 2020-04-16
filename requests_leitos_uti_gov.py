import requests
from datetime import date
import pandas as pd

# Função para retorna a quantidade de leitos UTI's por estado
def Leitos_UTI(uf):
    http = 'https://covid-insumos.saude.gov.br/paineis/insumos/graficos/uti.php?uf=' + uf + ''
    page = requests.get(http)
    UTI = page.text
    UTI = UTI[(UTI.find('data: [') + 7):]
    UTI = UTI[:UTI.find(',')]
    return UTI

# Função para retornar quantidade de leitos alocados por estado
def Leitos_Locados(uf):
    http = 'https://covid-insumos.saude.gov.br/paineis/insumos/graficos/graflocados.php?uf=' + uf + ''
    page = requests.get(http)
    UTI_LOC = page.text
    UTI_LOC= UTI_LOC[(UTI_LOC.find('data: [') + 7):]
    UTI_LOC = UTI_LOC[:UTI_LOC.find(',')]
    return UTI_LOC

# Lista com número dos estados
estados_num = ['11','12','13','14','15','16','17','21','22','23','24','25','26','27','28','29','21','31','32','33','35','50','51','52','53','41','42','43']

# Dicionário relacionando número do estado com sua unidade federativa 
dic_UF = {
    '11':'RO', '12':'AC', '13':'AM', '14':'RR', '15':'PA', '16':'AP', '17':'TO',
    '21':'MA', '22':'PI', '23':'CE', '24':'RN', '25':'PB', '26':'PE', '27':'AL', '28':'SE', '29':'BA',
    '31':'MG', '32':'ES', '33':'RJ', '35':'SP',
    '41':'PN', '42':'SC', '43':'RN',
    '50':'MS', '51':'MT', '52':'GO', '53':'DF'
}

ds = []

for x in estados_num:
    UF = dic_UF[x]
    LL = Leitos_Locados(x)
    LU = Leitos_UTI(x)
    append = [UF, LL, LU]
    ds.append(append)

# Cria o dataframe
UTI_SUS = pd.DataFrame(data = ds, columns = ['UF', 'Leitos locados', 'Leitos UTI'])
print(UTI_SUS)

