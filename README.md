# Access to Financial Markets
### Task
This project studies a key question in emerging economies: how do households differ in their access to financial markets?
I study this using household data from Mexico.

### Data
Household data from [Mexican Family Life Survey](http://www.ennvih-mxfls.org/english/)

### Notebooks
- 01_clean_household: clean household level data, study possession of illiquid assets
- 01_clean_individual: clean individual level data, form income measure 
- 02_merge_household_individual: combine household level data and individual level data
- 03_EDA: exploratory data analysis 
- 03_financial: study the determinants of access to financial markets

### Findings
- Access to financial markets increases with income and education, and varies significantly with industry and location.
- Younger households have higher education levels than older households.

### Data Wrangling
- Imputed missing income values using multivariate regression.
- Merged individual level and household level datasets.
- Removed income outliers.

### Tools
- Pandas - data wrangling
- Matplotlib/seaborn - visualization
- Statsmodels - logistic regression
