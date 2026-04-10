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

---

### Human Survival Index (HSI)

The Human Survival Index (HSI) aggregates multiple dimensions of survivability into a single normalized score. Each component represents a different aspect of a population’s ability to respond to and endure adverse conditions.

#### Categories

- **Health and Physical Fitness (HP):** obesity rates, physical disabilities, density of nursing homes  
- **Education and Awareness (EA):** education levels, density of schools  
- **Mobility and Escape (ME):** vehicle access, transit dependence, road density  
- **Social and Community Factors (SC):** age demographics, military or veteran populations, gun ownership rates, hunting and fishing licenses  
- **Infrastructure and Preparedness (IP):** off-grid capacity, preparedness culture, emergency response behavior (e.g., COVID protocols)  
- **Environmental and Geographic Factors (EG):** terrain, climate, and weather patterns  

Each category is normalized to a common scale (e.g., 0 to 1), allowing for weighted aggregation.

### Weighted Formula

$$
\text{HSI} =
w_{HP} \cdot HP +
w_{EA} \cdot EA +
w_{ME} \cdot ME +
w_{SC} \cdot SC +
w_{IP} \cdot IP +
w_{EG} \cdot EG
$$

Subject to:

$$
w_{HP} + w_{EA} + w_{ME} + w_{SC} + w_{IP} + w_{EG} = 1
$$

Such that:

$$
\text{HSI} =
0.25 \cdot SC +
0.20 \cdot HP +
0.15 \cdot IP +
0.15 \cdot EG +
0.15 \cdot ME +
0.10 \cdot EA
$$

---

### Modifying $\kappa$

The survivability index can be used to scale a base parameter $\kappa$:

$$
\kappa_{\text{adjusted}} = \kappa \cdot \left(1 + 0.5 \cdot \text{HSI}\right)
$$

---

### Research Questions:
1. What will the spread of the outbreak look like? ​
2. How rapidly will it progress? ​
3. Where are the most and least affected areas? ​
4. How do human factors modify your odds of survival?

---

## Code Repository Resources:
- https://github.com/epistorm/epydemix
- https://maplapse.readthedocs.io/en/latest/
- https://medium.com/tech-carnot/time-lapse-choropleth-map-visualization-using-geopandas-8adb77a7d14
- https://plotly.com/python/maps/
- https://plotly.com/python/tile-county-choropleth/
- https://plotly.com/python/bubble-maps/
- https://plotly.com/python/choropleth-maps/
- https://plotly.com/python/county-choropleth/

---
## Data File Naming Convention
```
nc_name_of_topic.csv
```
Examples:
```
nc_population.csv
nc_geography_and_weather.csv
```

---

## Data Resources:
Social and Community:
- Age Demographics: https://data.census.gov/table/ACSST5Y2023.S0101?g=010XX00US$0500000&moe=true
- Hunting and Fishing:
    - NC Game Harvests: https://www.ncwildlife.gov/hunting/harvest-statistics
- Gun Ownership:
    - Gun Ownership: https://schs.dph.ncdhhs.gov/data/brfss/2021/nc/all/GunStat.html
    - Country Classification: https://connect.ncdot.gov/events/Documents/nc-county-classifications.pdf
- Military and Veterans:
    - Veteran Populations: https://carolinademography.cpc.unc.edu/2021/05/27/who-are-north-carolinas-veterans/
    - Active Duty Military: https://www.remi.com/wp-content/uploads/2017/10/326-North-Carolina-General-Assembly-The-Economic-Impact-of-the-Military-on-North-Carolina-2013.pdf

Education and Awareness:
- 

Infrastructure and Preparedness:
- Census ACS S0101 (Prepper Density proxy): https://data.census.gov
- Oxford OxCGRT (COVID Compliance): https://github.com/OxCGRT/covid-policy-tracker
- Census ACS B25040 (Grid Independence): https://data.census.gov

Mobility and Escape:
- Census ACS B25044 (Vehicle Access / Transit Dependence): https://data.census.gov
- USDA RUCA Codes (Road Density): https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes  

Health and Physical Fitness:
- CDC PLACES (Obesity): https://data.cdc.gov/places
- Census ACS B18105 (Ambulatory Disability): https://data.census.gov
- CMS Care Compare (Nursing Homes): https://data.cms.gov/provider-data

Environment and Geography:
- Latitude, Longitude, Elevation, and Annual Precipitation: https://www.ncei.noaa.gov/data/normals-annualseasonal/1991-2020/access/

NC Resiliency
- NC Resiliency Scores by County: https://ncpro.nc.gov/north-carolina-economic-resilience-index 
