# Data requests about COVID-19 in Brazil

Data requests API on Brazilian Ministry of Health website about COVID-19. Checking the website's HTML, the script fetches the JSON file, where there are data from the world and Brazil COVID-19, however, the code filters only Brazilian data.

## Requirements
This code requires *Requests* and *Pandas* libraries installed.

## Output

The code output is a dataframe with the columns: date, uid (state ID), suspected cases, confirmed cases, refused cases and deaths. Example:


| index | date      | uid | suspects | cases | refuses | deaths |
|:-----:|:---------:|:---:|:--------:|:-----:|:-------:|:------:|
|1      |17/03/2020 |50   |44        |4      |45       |0       |
|2      |17/03/2020 |51   |23        |0      |7        |0       |
|3      |17/03/2020 |52   |221       |6      |54       |0       |
|4      |17/03/2020 |53   |253      |21      |96       |0       |
