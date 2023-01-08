import pandas as pd

df = pd.read_csv('./dataset/teams_data.csv', encoding='latin1', sep=';')
internationals = pd.read_csv('./dataset/input.csv', encoding='latin1', sep=';')

team_scores = {}
countries = set(internationals['home_team'])

# delete every row of the dataframe "df" where the value of the column "team" is not in the set "countries"
df = df[df['team'].isin(countries)]

# for each country in column "team", create a list containing the corresponding values of the mean of the columns "goalkeeper_score", "mean_defense_score", "mean_midfield_score" and "mean_offense_score"
for country in df['team']:
    team_scores[country] = df.loc[df['team'] == country, ['goalkeeper_score', 'mean_defense_score', 'mean_midfield_score', 'mean_offense_score']].mean().tolist()

# for each country in the dictionary "team_scores" set the values of the columns "goalkeeper_score", "mean_defense_score", "mean_midfield_score" and "mean_offense_score" to the values of the list
for country in team_scores:
    df.loc[df['team'] == country, ['goalkeeper_score', 'mean_defense_score', 'mean_midfield_score', 'mean_offense_score']] = team_scores[country]

# save the dataframe "df" to a csv file
df.to_csv('./dataset/modified_teams_data.csv', index=False, encoding='latin1', sep=',')