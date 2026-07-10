import pandas as pd
import xgboost as xgb

drivers = {
    1: "Max Verstappen", 3: "Lewis Hamilton", 4: "Lando Norris",
    5: "Oscar Piastri", 6: "George Russell", 7: "Charles Leclerc",
    8: "Carlos Sainz", 9: "Fernando Alonso", 10: "Lance Stroll",
    11: "Pierre Gasly", 12: "Esteban Ocon", 13: "Alexander Albon",
    14: "Nico Hulkenberg", 15: "Valtteri Bottas", 16: "Sergio Perez",
    17: "Oliver Bearman", 18: "Kimi Antonelli", 19: "Isack Hadjar",
    20: "Arvid Lindblad", 21: "Gabriel Bortoleto"
}

raw_data = {
    'driverId': [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
    'constructorId': [4, 2, 3, 3, 1, 2, 8, 10, 10, 5, 7, 8, 14, 11, 16, 17, 9, 7, 11, 1],
    'raceId': [1289] * 20,
    'year': [2026] * 20,
    'grid': [7, 3, 6, 8, 4, 2, 15, 18, 19, 12, 17, 16, 14, 20, 13, 11, 9, 10, 5, 1],
    'points': [128, 255, 179, 179, 333, 255, 11, 0, 0, 60, 21, 11, 6, 0, 6, 6, 6, 21, 0, 333]
}

df = pd.DataFrame(raw_data)

df['grid'] = df['grid'].replace(0, 20)
df['team_grid'] = df.groupby(['raceId', 'constructorId'])['grid'].transform('mean')
df['skill_diff'] = df['grid'] - df['team_grid']

features = ['points', 'constructorId', 'raceId', 'year', 'driverId', 'grid', 'team_grid', 'skill_diff']
X_test = df[features]

model = xgb.Booster()
model.load_model("f1_ranking_model.json")

test_matrix = xgb.DMatrix(X_test)
df['predicted_score'] = model.predict(test_matrix)

df['driver_name'] = df['driverId'].map(drivers)
results = df[['driver_name', 'predicted_score']].sort_values(by='predicted_score', ascending=False).reset_index(drop=True)

print(results)
