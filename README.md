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
\text{HSI} = w_H H + w_E E + w_M M + w_S S + w_I I + w_G G
$$
where:
$$
w_H + w_E + w_M + w_S + w_I + w_G = 1
$$
- $H$: Health and Physical Fitness  
- $E$: Education and Awareness  
- $M$: Mobility and Escape Resources  
- $S$: Social and Community Factors  
- $I$: Infrastructure and Preparedness  
- $G$: Environmental and Geographic Factors  

### Research Questions:
1. How does population density affect survival time?  
2. Where are the lowest-risk areas and potential escape zones?  
3. Do survivability modifiers meaningfully increase survival odds?  


## Code Repository Resources:
- https://github.com/epistorm/epydemix
- https://maplapse.readthedocs.io/en/latest/
- https://medium.com/tech-carnot/time-lapse-choropleth-map-visualization-using-geopandas-8adb77a7d14
- https://ncpro.nc.gov/north-carolina-economic-resilience-index


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
- Age Demographics: https://data.census.gov/table/ACSST5Y2023.S0101?g=010XX00US$0500000&moe=true
- Hunting and Fishing Licenses: https://partnerwithapayer.org/funding-sources/
- Gun Ownership and Sales:
    - Gun Ownership: https://ammo.com/articles/gun-ownership-by-state & https://worldpopulationreview.com/state-rankings/gun-ownership-by-state
    - Gun Sales: https://datahub.thetrace.org/dataset/gun-sales/
- Military and Veterans:
    - Veteran Populations: https://www.ruralhealthinfo.org/charts/97](https://carolinademography.cpc.unc.edu/2021/05/27/who-are-north-carolinas-veterans/
    - Active Duty Military and Government Civilians: https://dwp.dmdc.osd.mil/dwp/app/dod-data-reports/workforce-reports
- Environment and Geography:
    - Latitute, Longitude, Elevation, and Annual Precipitation: https://www.ncei.noaa.gov/data/normals-annualseasonal/1991-2020/access/
