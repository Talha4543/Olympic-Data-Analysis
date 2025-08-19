import numpy as np
import pandas as pd

def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df
    if year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df = medal_df[(medal_df['Year'] == int(year)) & (medal_df['region'] == country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum(numeric_only=True)[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum(numeric_only=True)[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                      ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']

    x[['Gold','Silver','Bronze','total']] = x[['Gold','Silver','Bronze','total']].astype(int)

    return x


def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')

    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'Overall')

    return years,country


def data_over_time(df, col):
    nations_over_time = (
        df.drop_duplicates(['Year', col])
          .groupby('Year')
          .count()
          .reset_index()[['Year', col]]
    )
    nations_over_time.rename(columns={'Year': 'Edition'}, inplace=True)
    return nations_over_time


def most_successful(df, sport):
    temp_df = df.dropna(subset=['Medal'])
    
    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]
    
    x = temp_df['Name'].value_counts().reset_index().head(15)
    x.columns = ['Name', 'Medals']
    
    x = x.merge(df, left_on="Name", right_on="Name", how="left")[['Name','Medals','Sport','region']].drop_duplicates('Name')
    
    return x


def yearwise_medal_tally(df, country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df = temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])

    new_df = temp_df[temp_df['region'] == country]
    final_df = new_df.groupby('Year').count()['Medal'].reset_index()

    return final_df


def country_event_heatmap(df, country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df = temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])

    new_df = temp_df[temp_df['region'] == country]

    pt = new_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0)
    return pt


import pandas as pd

def most_successful_countrywise(df, country):
    # Ensure 'Name' exists (some datasets use 'Athlete')
    if 'Name' not in df.columns:
        if 'Athlete' in df.columns:
            df = df.rename(columns={'Athlete': 'Name'})
        else:
            raise KeyError("Neither 'Name' nor 'Athlete' column exists in df.")

    if 'region' not in df.columns:
        raise KeyError("'region' column is missing. Make sure you merged region_df in preprocess().")

    if 'Sport' not in df.columns:
        raise KeyError("'Sport' column is missing from df.")

    # Keep medal-winning rows for the selected country
    temp = df[df['Medal'].notna() & (df['region'] == country)].copy()
    if temp.empty:
        # Return empty but correctly-typed frame instead of crashing
        return pd.DataFrame(columns=['Name', 'Medals', 'Sport'])

    # Medal count per athlete
    medal_counts = (
        temp.groupby('Name', as_index=False)
            .size()
            .rename(columns={'size': 'Medals'})
    )

    # Most common sport per athlete (break ties by Sport name for determinism)
    sport_counts = (
        temp.groupby(['Name', 'Sport'], as_index=False)
            .size()
    )
    sport_mode = (
        sport_counts.sort_values(['Name', 'size', 'Sport'], ascending=[True, False, True])
                    .drop_duplicates('Name')[['Name', 'Sport']]
    )

    # Top 10 by medals + their primary sport
    top10 = (
        medal_counts.sort_values('Medals', ascending=False)
                    .head(10)
                    .merge(sport_mode, on='Name', how='left')
    )

    return top10


import seaborn as sns
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import seaborn as sns

def weight_v_height(df, sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    athlete_df['Medal'] = athlete_df['Medal'].fillna('No Medal')
    
    # filter by sport if selected
    if sport != 'Overall':
        temp_df = athlete_df[athlete_df['Sport'] == sport]
    else:
        temp_df = athlete_df

    # create figure and plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        x="Weight",
        y="Height",
        hue="Medal",
        style="Sex",
        s=60,
        data=temp_df,
        ax=ax
    )

    return fig


def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()

    final = men.merge(women, on='Year', how='left')
    final.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)

    final.fillna(0, inplace=True)

    return final
