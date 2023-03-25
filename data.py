import pandas as pd
import numpy as np


df_it = pd.read_csv(r'data/time_series_60min_singleindex_filtered.csv', sep=',')

#df_it = df_it.to_datetime['cet_cest_timestamp']

df_it['cet_cest_timestamp'] = pd.to_datetime(df_it['cet_cest_timestamp'])

# Convert the 'IT_load_actual_entsoe_transparency' column to float format
df_it['IT_load_actual_entsoe_transparency'] = df_it['IT_load_actual_entsoe_transparency'].astype(float)

print(df_it.columns)