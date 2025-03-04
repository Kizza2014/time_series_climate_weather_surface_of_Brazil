# Download data:
curl -L -o ~/hourly-weather-surface-brazil-southeast-region.zip https://www.kaggle.com/api/v1/datasets/download/PROPPG-PPG/hourly-weather-surface-brazil-southeast-region

unzip hourly-weather-surface-brazil-southeast-region.zip

mkdir data

mv *.csv data
# Preprocess data and plot time series graph:
All is in file `eda.ipynb`

Final data is in `prcp_monthly.csv`

# Basic analysis:
Using `analysis.ipynb`

# Fitting models:
### AR(1):
- MSE: 7802.46
- MAE: 72.75
- R2: 0.010
- Low performance due to seasonality.
  
### OLS:
- Quaterlity (linear model):
  - MSE: 1756.59
  - RMSE: 41.91
  - MAE: 33.34
  - R2: 0.764
  - AIC: 1899.79
  - BIC: 1915.75
- Monthly (linear model):
  - MSE: 1087.24
  - RMSE: 32.97
  - MAE: 24.86
  - R²: 0.854
  - AIC: 1824.68
  - BIC: 1866.19

### Exponential smoothing family:
##### Holt Winters:
- MSE: 1077.66
- RMSE: 32.83
- MAE: 24.71
- R2: 0.855
- AIC: 1327.97
- BIC: 1372.67

##### ETS:
- MSE: 1057.33
- RMSE: 32.52
- MAE: 24.26
- R2: 0.858
- AIC: 1830.95
- BIC: 1882.04
