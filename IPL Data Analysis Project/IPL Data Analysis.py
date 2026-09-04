import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_column',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.width',None)

df = pd.read_csv('ipl.22.csv')
print(df)

df.head()
df.info()
print(f"your rows are{df.shape[0]} and your columns are {df.shape[1]}")
print(df.isnull().sum())

"""subplots bnaa k in sb ko draw krny ki koshis ki thi lekin nhii hoa"""
fig = plt.figure(8,5)
fig.subplots(4,4)

plt.subplots(4,4,1)

"""match win barplot use krty hoye"""
match_win = df['match_winner'].value_counts()
sns.barplot(y = match_win.index , x =match_win.values,palette='rainbow')
plt.title('most match win by team')

"""countplot k through """
sns.countplot(x = df['toss_decision'])
plt.title("Toss Decison Trends")

"""Toss winner vs Match winner"""
toss_and_winner_count = df[df["toss_winner"]==df["match_winner"]]['match_id'].count()
mean = ((toss_and_winner_count / df.shape[0]) * 100)
print(mean.round(2))

"""how do teams win? (runs vs wickets)"""
sns.countplot(x=df['won_by'])
plt.title('Won By')

"""Key Player Performance___player of the match"""
player_of_match = df["player_of_the_match"].value_counts().head(10)
print(player_of_match)
sns.barplot(y = player_of_match.index , x = player_of_match.values,palette='rainbow')
plt.title("Top 10 player")

"""2 Top Scorars"""
top_scorars = df.groupby('top_scorer')["highscore"].sum().sort_values(ascending=False).head(2)
print(top_scorars)
top_scorars.plot(kind = 'barh')

"""10 Best Bowling Figures"""
def fa(a):
    return a.split('--')[0]
#jb new column bnaya to oska data type hmeesha string rhyy ga
df['highest_wickets'] = df['best_bowling_figures'].apply(fa)
df['highest_wickets'] = df['highest_wickets'].astype(int)
top_bowlers = df.groupby('best_bowling')["highest_wickets"].sum().sort_values(ascending=False).head(10)
print(top_bowlers)
sns.barplot( y= top_bowlers.index , x = top_bowlers.values,palette ='rainbow')

"""most match played by vanue"""
venue_count = df['venue'].value_counts()
print(venue_count)
sns.barplot(y = venue_count.index,x = venue_count.values)

"""who won the highest margin by runs"""
print(df[df["won_by"] == 'Runs'].sort_values(by="margin",ascending=False).head(1)[['match_winner',"margin"]])

"""which player had the highest individual score"""
print(df[df['highscore']==df['highscore'].max()][["top_scorer","highscore"]])

"""which bowler had the best bowling figure"""
def fa(a):
    return a.split('--')[0]
#jb new column bnaya to oska data type hmeesha string rhyy ga
df['highest_wickets'] = df['best_bowling_figures'].apply(fa)
df['highest_wickets'] = df['highest_wickets'].astype(int)

print(df[df['highest_wickets'] == df['highest_wickets'].max()]["best_bowling","best_bowling_figure"])

plt.show()