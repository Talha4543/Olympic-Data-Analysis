import pandas as pd

def preprocess(df, region_df):
    df = df[df['Season'] == 'Summer'].copy()
    df = df.merge(region_df, on='NOC', how='left')
    if 'Athlete' in df.columns and 'Name' not in df.columns:
        df.rename(columns={'Athlete': 'Name'}, inplace=True)
    df.drop_duplicates(inplace=True)
    if 'Medal' in df.columns:
        df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df
