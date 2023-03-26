import pandas as pd


df_it_draft = pd.read_csv(r'data/time_series_60min_singleindex_filtered.csv', sep=';')

# Convert column to datetime format and remove timezone offset
def convert_df(df):
    print('Convert type process ...')
    df['cet_cest_timestamp'] = pd.to_datetime(
    df['cet_cest_timestamp'],
    format='%Y-%m-%d %H:%M:%S%z',
    utc=True).dt.tz_convert(None)
    df['IT_load_actual_entsoe_transparency'] = df['IT_load_actual_entsoe_transparency'].astype(float)
    print('Successful')
    return df

df_it = convert_df(df_it_draft)
