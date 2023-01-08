import pandas as pd

df = pd.read_csv('./datasets/international_matches.csv', encoding='latin1', sep=';')

home_team = df['home_team']
home_team_fifa_rank = df['home_team_fifa_rank']
home_team_total_fifa_points = df['home_team_total_fifa_points']

fifa_rank = {}
fifa_points = {}

for country, score in zip(home_team.iloc[::-1], home_team_fifa_rank.iloc[::-1]):
    if country not in fifa_rank:
        fifa_rank[country] = score

fifa_rank = dict(sorted(fifa_rank.items()))

for country, score in zip(home_team.iloc[::-1], home_team_total_fifa_points.iloc[::-1]):
    if country not in fifa_points:
        fifa_points[country] = score

fifa_points = dict(sorted(fifa_points.items()))

result = pd.read_csv("./dataset/input.csv")

for k, v in fifa_rank.items():
    result.loc[result["home_team"] == k, "home_team_fifa_rank"] = v

for k, v in fifa_rank.items():
    result.loc[result["away_team"] == k, "away_team_fifa_rank"] = v

for k, v in fifa_points.items():
    result.loc[result["home_team"] == k, "home_team_total_fifa_points"] = v

for k, v in fifa_points.items():
    result.loc[result["away_team"] == k, "away_team_total_fifa_points"] = v

result.to_csv("./datasets/results.csv", index=False)