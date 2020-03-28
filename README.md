# Data requests about COVID-19 in Brazil

Data requests API about COVID-19 cases in Brazil. Checking the website, the script fetches the JSON file, where there are data from  
confirmed cases. There are two data sources in the script:
- BING site: returns by state the number of confirmed cases, deaths and recovered cases
- Site Globo: returns by date and city the number of confirmed cases.

## Requirements
This code requires *Requests* and *Pandas* libraries installed.

## Output

### BING Case:

The code output is a dataframe with the columns: date, uid (state ID), suspected cases, confirmed cases, refused cases and deaths. Example:


| Index | Estado  | Casos Confirmados | Óbitos | Casos recuperados |
|:-----:|:-------:|:------------------|:------:|:-----------------:|
|0      |Acre     |25                 |NaN     |None               |
|1      |Amazonas |81                 |1.0     |None               |
|2      |Amapá    |2                  |NaN     |None               |
|3      |Pará     |13                 |NaN     |None               |
...

### Globo Case:


| Index | Data      | Cidade     | Estado | Casos Confirmados |
|:-----:|:---------:|:----------:|:------:|:-----------------:|
|0      |2020-02-26 |São Paulo   |SP      |1                  |     
|1      |2020-02-26 |São Paulo   |SP      |1                  |
|2      |2020-02-26 |São Paulo   |SP      |1                  |
|3      |2020-02-26 |Barra Mansa |RJ      |1                  |
|3      |2020-02-26 |Vila Velha  |ES      |1                  |
...
|713    |2020-03-27 |Fortaleza   |CE      |45                 |
|714    |2020-03-27 |Araguaína   |TO      |1                  |
|715    |2020-03-27 |Macapá      |AP      |1                  |
