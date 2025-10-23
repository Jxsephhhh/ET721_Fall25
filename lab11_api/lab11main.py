"""
Joseph Bernabe
Oct 22, 2025
Lab 11, API's
"""
import pandas as pd 

# -----------------
# 1. Example dataframe
# -----------------
dict_ = {'a':[11,21,31], 'b':[12,22,32]}

# create a dataframe fro dict_
df = pd.DataFrame(dict_)

# display the first few rows of the dataframe
print(df.head())

# mean method calulates and return the mean of the data
print(df.mean())

# -----------------
# 2. Get NBA teams
# -----------------
from static import get_teams

# the method get_teams() return a list of dictionaries 
nba_teams = get_teams()
print(f"First 2 teams: {nba_teams[:2]}")

# convert list of dictionaries into dataframe
df_teams = pd.DataFrame(nba_teams)
print(df_teams.head())

# find the id of the arriors 
df_warrior = df_teams[df_teams["nickname"]== "Warriors"]
print(f"warrior {df_warrior}")

# find the iod of the warriors using the information in the first column
warrior_id = df_warrior[["id"]].values[0][0]
print(f"\nWarrior id = {warrior_id}")

# ----------------
# 3. Get NBA teams
# ----------------

import requests

url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/" "CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl" 

file_name = "Golden_state.pk1"
print("\n Downloading external data")
response = requests.get(url)

if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("download complete")
else:
    print("download failed")

# b. load dataframe from pickle 
games = pd.read_pickle(file_name)
print("\nGames data from picle file:")
print(games.head())

#c. filter GSW vs Raptors
warriors_vs_raptors = games[games['MATCHUP'].str.contains("TOR")]

gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors
["MATCHUP"].str.contains(" vs. ")]

gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors
["MATCHUP"].str.contains(" @ ")]

# d. calculate averages 
home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()
home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
away_avg_pts = gsw_away_vs_raptors['PTS'].mean()

print(f"\nWarriors home average {home_avg_plus}")
print(f"\nWarriors away average {away_avg_plus}")

# e. visulation 
import matplotlib.pyplot as plt 

metrics = ["PLUS_MINUS", "PTS"]
home_values = [home_avg_plus, home_avg_pts]
away_values = [away_avg_plus, away_avg_pts]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8,5))
plt.bar([i - bar_width/2 for i in x], home_values,width=bar_width, label = "Home", color = "skyblue")
plt.bar([i + bar_width/2 for i in x], away_values, width = bar_width, label="Away", color="orange")

plt.xticks(x,metrics)
plt.title("Golden State Warriors vs. Raptors - Home vs Away comparson")
plt.ylabel("Average value")
plt.grid(axis="y", linestyle = "--", alpha=0.7)
plt.tight_layout()
plt.show()

input("Press Enter to close...")