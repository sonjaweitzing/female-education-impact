# Women's educational attainment vs. fertility rate - Data package

This data package contains the data that powers the chart ["Women's educational attainment vs. fertility rate"](https://ourworldindata.org/grapher/womens-educational-attainment-vs-fertility?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website.

## CSV Structure

The high level structure of the CSV file is that each row is an observation for an entity (usually a country or region) and a timepoint (usually a year).

The first two columns in the CSV file are "Entity" and "Code". "Entity" is the name of the entity (e.g. "United States"). "Code" is the OWID internal entity code that we use if the entity is a country or region. For normal countries, this is the same as the [iso alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the entity (e.g. "USA") - for non-standard countries like historical countries these are custom codes.

The third column is either "Year" or "Day". If the data is annual, this is "Year" and contains only the year as an integer. If the column is "Day", the column contains a date string in the form "YYYY-MM-DD".

The remaining columns are the data columns, each of which is a time series. If the CSV data is downloaded using the "full data" option, then each column corresponds to one time series below. If the CSV data is downloaded using the "only selected data visible in the chart" option then the data columns are transformed depending on the chart type and thus the association with the time series might not be as straightforward.

## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc.. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc..

## About the data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stich together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

### How we process data at Our World In Data
All data and visualizations on Our World in Data rely on data sourced from one or several original data providers. Preparing this original data involves several processing steps. Depending on the data, this can include standardizing country names and world region definitions, converting units, calculating derived indicators such as per capita measures, as well as adding or adapting metadata such as the name or the description given to an indicator.
[Read about our data pipeline](https://docs.owid.io/projects/etl/)

## Detailed information about each time series


## Fertility rate, total – UN WPP
The average number of live births a hypothetical cohort of women would have at the end of their reproductive period if they were subject during their whole lives to the fertility rates of a given period and if they were not subject to mortality.
Last updated: July 12, 2024  
Date range: 1950–2023  
Unit: live births per woman  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
UN, World Population Prospects (2024) – processed by Our World in Data

#### Full citation
UN, World Population Prospects (2024) – processed by Our World in Data. “Fertility rate, total – UN WPP” [dataset]. United Nations, “World Population Prospects” [original data].
Source: UN, World Population Prospects (2024) – processed by Our World In Data

### What you should know about this data
* It is expressed as live births per woman. For age-specific fertility rates, it measures the number of births to women in a particular age group, divided by the number of women in that age group. The age groups used are: 15-19, 20-24, ..., 45-49. The data refer to annual civil calendar years from 1 January to 31 December.

### Source

#### United Nations – World Population Prospects
Retrieved on: 2024-07-11  
Retrieved from: https://population.un.org/wpp/Download/  


## Average years of schooling (women aged 15–64)
Average years of formal education for women aged 15-64.
Last updated: July 17, 2023  
Date range: 1870–2040  
Unit: years  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Barro and Lee (2015); Lee and Lee (2016) – with major processing by Our World in Data

#### Full citation
Barro and Lee (2015); Lee and Lee (2016) – with major processing by Our World in Data. “Average years of schooling (women aged 15–64)” [dataset]. Barro and Lee, “Projections of Educational Attainment”; Lee and Lee, “Human Capital in the Long Run” [original data].
Source: Barro and Lee (2015), Lee and Lee (2016) – with major processing by Our World In Data

### What you should know about this data
* For the years leading up to 2015, the data are derived from historical estimates, providing a retrospective view of education levels. For the years 2015 and beyond, the projections are grounded in the historical data of 2010, which serve as the foundational benchmark. These forward-looking projections are then crafted by analyzing trends in school enrollment and changes in population structures. These trends are informed by forecasts from the United Nations, ensuring a global perspective and understanding of future educational developments.
* The method to estimate average years of schooling takes into account the age distribution in the population. This is important because access to education can vary significantly across generations. Older generations may have had fewer educational opportunities than younger ones, which affects the overall average education level.
* It also considers the typical duration required to complete each education level. For instance, primary education usually takes about 6 years, secondary education 4-6 years, and higher education may take even longer. Understanding the time investment required for different education levels is essential for accurate assessment.
* At its core, the method calculates the average years of schooling. This is achieved by determining the percentage of the population that has completed each education level and multiplying it by the duration of that level. The sum of these results gives a comprehensive view of both the extent of educational attainment and the time spent in education by the population.
* The method is dynamic, adapting to changes over time and across regions. For example, if a country increases the length of primary education, this change is included in subsequent calculations. This adaptability ensures that the average years of education remain relevant and accurate over time and across different educational systems.
* Note that the method does not take into account the quality of education. It only considers the number of years spent in education. This means that the average years of schooling may not reflect the actual skills and knowledge of the population.

### Sources

#### Barro and Lee – Projections of Educational Attainment
Retrieved on: 2023-11-20  
Retrieved from: http://www.barrolee.com/  

#### Lee and Lee – Human Capital in the Long Run
Retrieved on: 2023-11-20  
Retrieved from: https://barrolee.github.io/BarroLeeDataSet/DataLeeLee.html  

#### Notes on our processing step for this indicator
Historical data up to the year 2010 has been sourced from 'Human Capital in the Long Run' by Lee and Lee (2016). This historical data was then combined with recent projections provided by Barro ane Lee (2015).

Regional aggregates were computed by Our World in Data through yearly population-weighted averages, where annual values are proportionally adjusted to emphasize the influence of larger populations.



## Population (historical)
Population by country, available from 10,000 BCE to 2023, based on data and estimates from different sources.
Last updated: July 15, 2024  
Next update: July 2026  
Date range: 10000 BCE – 2023 CE  
Unit: people  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
HYDE (2023); Gapminder (2022); UN WPP (2024) – with major processing by Our World in Data

#### Full citation
HYDE (2023); Gapminder (2022); UN WPP (2024) – with major processing by Our World in Data. “Population (historical)” [dataset]. PBL Netherlands Environmental Assessment Agency, “History Database of the Global Environment 3.3”; Gapminder, “Population v7”; United Nations, “World Population Prospects”; Gapminder, “Systema Globalis” [original data].
Source: HYDE (2023); Gapminder (2022); UN WPP (2024) – with major processing by Our World In Data

### Sources

#### PBL Netherlands Environmental Assessment Agency – History Database of the Global Environment
Retrieved on: 2024-01-02  
Retrieved from: https://doi.org/10.24416/UU01-AEZZIT  

#### Gapminder – Population
Retrieved on: 2023-03-31  
Retrieved from: http://gapm.io/dpop  

#### United Nations – World Population Prospects
Retrieved on: 2024-07-11  
Retrieved from: https://population.un.org/wpp/Download/  

#### Gapminder – Systema Globalis
Retrieved on: 2023-03-31  
Retrieved from: https://github.com/open-numbers/ddf--gapminder--systema_globalis  

#### Notes on our processing step for this indicator
### Combination of different sources
The population data is constructed by combining data from multiple sources:

- 10,000 BCE - 1799: Historical estimates by HYDE (v3.3).

- 1800 - 1949: Historical estimates by Gapminder (v7).

- 1950-2023: Population records by the UN World Population Prospects (2024 revision).

### Regional aggregates

**Continents and other region aggregates**:

For most of the years, we've estimated regional aggregates by summing the population of countries in each region. We've relied on [our continents](https://ourworldindata.org/world-region-map-definitions#our-world-in-data) and [World Bank income group definitions](https://ourworldindata.org/grapher/world-bank-income-groups). The only exception is before 1800, where we've used HYDE's estimates on continents (but not income groups).

**World**:
- Before 1800: We've used HYDE's estimates.
- 1800-1950: We've estimated the World population by summing all available countries in the dataset, ensuring that we do not double-count any country.
- After 1950: We've relied on UN WPP's estimates.


## World regions according to OWID
Last updated: January 1, 2023  
Date range: 2023–2023  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Our World in Data – processed by Our World in Data

#### Full citation
Our World in Data – processed by Our World in Data. “World regions according to OWID” [dataset]. Our World in Data, “Regions” [original data].
Source: Our World in Data

### What you should know about this data

### Source

#### Our World in Data – Regions


    