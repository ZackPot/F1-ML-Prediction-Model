import pandas as pd
import xgboost as xgb

df = pd.read_csv('final_data.csv')
print(df.columns)

X = df.drop(columns=['positionOrder', 'name'])
y = df['positionOrder']

groups = df.groupby("raceId").size().to_list()

model = xgb.XGBRanker(objective="rank:ndcg", eval_metric="ndcg")
model.fit(X, y, group=groups)

model.save_model('f1_ranking_model.json')