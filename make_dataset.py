import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf,pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

renamed_columns = ['data','hora','precipitacao total,horario (mm)','pressao atmosferica ao nivel da estacao (mb)','pressao atmosferica max. na hora ant. (aut) (mb)','pressao atmosferica min. na hora ant. (aut) (mb)','radiation (kj/m2)','temperatura do ar - bulbo seco (°c)','temperatura do ponto de orvalho (°c)','temperatura maxima na hora ant. (aut) (°c)','temperatura minima na hora ant. (aut) (°c)','temperatura orvalho max. na hora ant. (aut) (°c)','temperatura orvalho min. na hora ant. (aut) (°c)','umidade rel. max. na hora ant. (aut) (%)','umidade rel. min. na hora ant. (aut) (%)','umidade relativa do ar, horaria (%)','vento direcao horaria (gr) (° (gr))','vento rajada maxima (m/s)','vento velocidade horaria (m/s)','region','state','station','station_code','latitude','longitude','height']
renamed_columns_en = ['date','hour','total precipitation (mm)','pressao atmosferica ao nivel da estacao (mb)','atmospheric pressure max. in the previous hour (mb)','atmospheric pressure min. in the previous hour (mb)','radiation (kj/m2)','air temperature - dry bulb (°c)','dew point temperature (°c)','max. temperature in the previous hour (°c)','min. temperature in the previous hour (°c)','dew temperature max. in the previous hour (°c)','dew temperature min. in the previous hour (°c)','relative humidity max. in the previous hour (%)','relative humidity min. in the previous hour (%)','air relative humidity (%)','wind direction (° (gr))','wind rajada maxima (m/s)','wind speed (m/s)','region','state','station','station_code','latitude','longitude','height']
abbreviation = ['date','hour','prcp', 'stp', 'smax', 'smin','gbrd','temp','dewp','tmax','tmin','dmax','dmin','hmax','hmin','hmdy','wdct', 'gust', 'wdsp', 'regi','prov','wsnm','inme','lat','lon','elvt']

def process_raw(df):
    """
    ! drop index
    ! rename the columns
    ! combine hour and date columns -> transform to date_time
    ! append columns data from all stations to keep the data granularity
    ! remove unimportant columns
    ! return table 
    """
    df.drop(['index'],inplace=True, axis=1)
    df.columns = abbreviation
    df.drop(['regi','prov','wsnm','lat','lon','elvt'], inplace=True, axis=1)
    return df

def clean_na(df, na_value = -9999):
    """ 
    ! replace Na from dataset
    """
    df = df.replace(to_replace=na_value,value=np.NaN)
    df = df[df.iloc[:,1].first_valid_index():]
    df = df.ffill()
    return df

def make_dataset(start_date, df):
    """
    ! filter raw data from date and stations code
    ! process data
    ! clean na
    """
    df = df[df['Data'] >= start_date]
    df = process_raw(df)
    df = clean_na(df)
    return df.reset_index()
