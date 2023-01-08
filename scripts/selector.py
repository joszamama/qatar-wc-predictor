import pandas as pd

df = pd.read_csv('./dataset/modified_teams_data.csv', encoding='latin1', sep=',')
df = df.iloc[::-1]

internationals = pd.read_csv('./dataset/input.csv', encoding='latin1', sep=';')
countries = set(internationals['home_team'])

# create a new empty dataframe
df2 = pd.DataFrame()

for country in df['team'].unique():
    if country in countries:
        #export the first row of the dataframe "df" where the value of the column "team" is equal to the value of the variable "country" to dataframe "df2"
        df2 = df2.append(df.loc[df['team'] == country].iloc[0])

# delete columns "home_team_score" and "team_result" from dataframe "df2"
df2 = df2.drop(['home_team_score', 'team_result'], axis=1)

# save the dataframe "df2" to a csv file
df2.to_csv('./dataset/kmedias_input.csv', index=False, encoding='latin1', sep=',')