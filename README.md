# you-can-run-you-can-hide-the-zombie-apocalypse-

## Project Overview

### Model 
$$
\dot{S} = -\beta S Z
$$
$$
\dot{Z} = (\beta - \kappa) S Z
$$
$$
\dot{R} = \kappa S Z
$$
- **S** = Susceptible population (uninfected humans)  
- **Z** = Infected population (zombies)  
- **R** = Removed population (zombies destroyed by humans)  
- **β (beta)** = Bite rate (speed of infection spread)  
- **κ (kappa)** = Kill rate (effectiveness of humans against zombies)

### Human Survival Index (HSI)
The Human Survival Index will incorporate several categories of survivability modifiers. 
- **Health and Physical Fitness:** obesity rates, physical disabilities, density of nursing homes
- **Education and Awareness:** education levels, density of schools
- **Mobility and Escape:** vehicle access, transit dependence, road density
- **Social and Community Factors:** age demographics, military or veteran populations, gun ownership rates, hunting and fishing licenses
- **Infrastructure and Preparedness:** cities off the grid, doomsday preppers, COVID reactions/protocols
- **Environmental and Geographic Factors:** terrain, weather

Each category can itself be normalized around 0.

**Weighted Formula**

$$
\text{HSI} =
w_{ \text{HP} }\cdot \text{HP} + w_{ \text{EA} }\cdot \text{EA} + w_{ \text{ME} }\cdot \text{ME} + w_{ \text{SC} }\cdot \text{SC} + w_{ \text{IP} }\cdot \text{IP} + w_{ \text{EG} }\cdot \text{EG}
$$


where:

$$
w_{HP} + w_{EA} + w_{ME} + w_{SC} + w_{IP} + w_{EG} = 1
$$

- $HP$: Health and Physical Fitness  
- $EA$: Education and Awareness  
- $ME$: Mobility and Escape Resources  
- $SC$: Social and Community Factors  
- $IP$: Infrastructure and Preparedness  
- $EG$: Environmental and Geographic Factors  

### Research Questions:
1. What will the spread of the outbreak look like? ​
2. How rapidly will it progress? ​
3. Where are the most and least affected areas? ​
4. How do human factors modify your odds of survival?

## Code Repository Resources:
- https://github.com/epistorm/epydemix
- https://maplapse.readthedocs.io/en/latest/
- https://medium.com/tech-carnot/time-lapse-choropleth-map-visualization-using-geopandas-8adb77a7d14


## File Naming Convention
```
nc_name_of_topic.csv
```
Examples:
```
nc_population.csv
nc_geography_and_weather.csv
```

## Data Resources:
Social and Community Factors
- Age Demographics: https://data.census.gov/table/ACSST5Y2023.S0101?g=010XX00US$0500000&moe=true
- Hunting and Fishing:
    - NC Game Harvests: https://www.ncwildlife.gov/hunting/harvest-statistics
- Gun Ownership:
    - Gun Ownership: https://schs.dph.ncdhhs.gov/data/brfss/2021/nc/all/GunStat.html
    - Country Classification: https://connect.ncdot.gov/events/Documents/nc-county-classifications.pdf
- Military and Veterans:
    - Veteran Populations: https://carolinademography.cpc.unc.edu/2021/05/27/who-are-north-carolinas-veterans/
    - Active Duty Military: https://www.remi.com/wp-content/uploads/2017/10/326-North-Carolina-General-Assembly-The-Economic-Impact-of-the-Military-on-North-Carolina-2013.pdf
- Environment and Geography:
    - Latitute, Longitude, Elevation, and Annual Precipitation: https://www.ncei.noaa.gov/data/normals-annualseasonal/1991-2020/access/
- NC Resiliency Scores by County:
    - https://ncpro.nc.gov/north-carolina-economic-resilience-index 

