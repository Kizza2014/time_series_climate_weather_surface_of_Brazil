# Download data:
curl -L -o ~/hourly-weather-surface-brazil-southeast-region.zip https://www.kaggle.com/api/v1/datasets/download/PROPPG-PPG/hourly-weather-surface-brazil-southeast-region

unzip hourly-weather-surface-brazil-southeast-region.zip

mkdir data

mv *.csv data
# Preprocess data and plot time series graph:
All is in file `eda.ipynb`

# Basic analysis:
Using `analysis.ipynb`

# Fitting models:
AR(1):
- MSE: 7802.46
- MAE: 72.75
- R2: 0.010
- Low performance due to seasonality.
  
OLS:
- Quaterlity (linear model):
  - MSE: 3116.69
  - MAE: 47.12
  - R2: 0.605
- Monthly (linear model):
  - MSE: 2554.62
  - MAE: 43.41
  - R2: 0.676
