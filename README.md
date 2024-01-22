# Access to Financial Markets
### Task
This project studies a key question in emerging economies: how do households differ in their access to financial markets?
I study this using household data from Mexico.

### Data
Household data from [Mexican Family Life Survey](http://www.ennvih-mxfls.org/english/)

### Notebooks
- EDA
  - Perform exploratory data analysis of demographic variables.
- Financial
  - Explore the relationship between demographic variables and access to financial markets.

### Findings
- Access to financial markets increases with income, and varies significantly with industry and location.
- Younger households have higher education levels than older households.

### Data Wrangling
- Imputed missing income values using regression
- Merged individual level and household level datasets
- Removed income outliers

### Tools
- Pandas - data wrangling
- Matplotlib/seaborn - visualization
- Statsmodels - logistic regression
