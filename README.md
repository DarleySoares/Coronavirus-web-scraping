# Coronavirus web scraping

Checking the website, the script fetches the datas, where there are data from confirmed cases, deaths, intensive care unit and etc.

## Scripts
- request_covid_labs_wesley_costa: returns by date and state the number of confirmed cases and deaths.
- request_covid_globo: returns by date and city the number of confirmed cases.
- request_leitos_uti_gov: returns by state the number of intensive care unit

## Requirements
This code requires *Requests*, *Json* and *Pandas* libraries installed.

## Output

### Labs Wesley Costa:

| Index | Data      | Country | State  | City | NewDeaths | Deaths | NewCases | Total Cases | DeathsMS | TotalCasesMS  |
|:-----:|:---------:|:-------:|:------:|:----:|:---------:|:------:|:--------:|:-----------:|:--------:|:-------------:|
|0      |2020-02-26 |Brasil   |SP      |TOTAL |0          |0       |0         |0            |0         |0              |
|1      |2020-02-26 |Brasil   |SP      |TOTAL |0          |0       |0         |0            |0         |0              |
...

### Globo:

| Index | Data      | Cidade     | Estado | Casos Confirmados |
|:-----:|:---------:|:----------:|:------:|:-----------------:|
|0      |2020-02-26 |São Paulo   |SP      |1                  |     
|1      |2020-02-26 |São Paulo   |SP      |1                  |
|2      |2020-02-26 |São Paulo   |SP      |1                  |
...

### Leitos UTI (Ministério da Saúde)

| Index | UF    | Leitos locados | Leitos UTI |
|:-----:|:-----:|:--------------:|:----------:|
|0      |RO     |0               |231         |   
|1      |AC     |0               |48          |
|2      |AM     |0               |264         |
...
