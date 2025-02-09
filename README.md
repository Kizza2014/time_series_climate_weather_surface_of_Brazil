# Download data:
curl -L -o ~/hourly-weather-surface-brazil-southeast-region.zip https://www.kaggle.com/api/v1/datasets/download/PROPPG-PPG/hourly-weather-surface-brazil-southeast-region

unzip hourly-weather-surface-brazil-southeast-region.zip

mkdir data

mv *.csv data
# Preprocess data and plot time series graph:
All is in file `eda.ipynb`
