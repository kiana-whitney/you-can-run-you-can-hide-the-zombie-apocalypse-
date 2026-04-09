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
- **Social and Community Factors:** age demographics, military or veteran populations, gun ownership rates, hunting and fishing licenses
- **Infrastructure and Preparedness:** cities off the grid, doomsday preppers, COVID reactions/protocols
- **Environmental and Geographic Factors:** terrain, weather

Each category can itself be normalized around 0.

**Weighted Formula**
$$
\text{HSI} = w_{H\&P} \cdot H\&P + w_{E\&A} \cdot E\&A + w_{M\&E} \cdot M\&E + w_{S\&C} \cdot S\&C + w_{I\&P} \cdot I\&P + w_{E\&G} \cdot E\&G
$$

where:

$$
w_{H\&P} + w_{E\&A} + w_{M\&E} + w_{S\&C} + w_{I\&P} + w_{E\&G} = 1
$$

- $H\&P$: Health and Physical Fitness  
- $E\&A$: Education and Awareness  
- $M\&E$: Mobility and Escape Resources  
- $S\&C$: Social and Community Factors  
- $I\&P$: Infrastructure and Preparedness  
- $E\&G$: Environmental and Geographic Factors  

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

