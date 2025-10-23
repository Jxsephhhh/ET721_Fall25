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
df_warrior = df_teams[df_teams["nickname"]== "Warrior"]
print(df_warrior)

# find the id of the warriors using the information in the first column
warrior_id = df_warrior[["id"]].values[0][0]
print(f"\nWarrior id = {warrior_id}")

# -----------------
# 3. Download the pickle file
# -----------------

import requests

