import pandas as pd

standings_construct = pd.read_csv('RawData/constructor_standings.csv')
races = pd.read_csv('RawData/races.csv')
results = pd.read_csv('RawData/results.csv')

df = pd.merge(standings_construct[['points', 'constructorId', 'raceId']],
              races[['year', 'name', 'raceId']], on='raceId', how='left')

df = pd.merge(df, results[['raceId', 'constructorId', 'driverId', 'grid', 'positionOrder']],
              on=['raceId', 'constructorId'], how='left')

df = df[df['year'] >= 2017]
df = df[df['year'] != 2026]
df['positionOrder'] = 21 - df['positionOrder']

df['team_grid'] = df.groupby(['raceId', 'constructorId'])['grid'].transform('mean')
df['skill_diff'] = df['grid'] - df['team_grid']

df['grid'] = df['grid'].replace(0, 20)
df.sort_values(by='raceId', inplace=True)

df.to_csv('final_data.csv', index=False)