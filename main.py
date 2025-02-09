import pandas as pd
from make_dataset import make_dataset

data_path = 'data/central_west.csv'
df = pd.read_csv(data_path)
print('Load dataframe successfully')

df = make_dataset(start_date='2001-01-01', df=df)
print(df.head())