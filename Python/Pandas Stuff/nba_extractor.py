# This script operates on an 'NBA Player Performance Stats' dataset
# downloaded from Kaggle. It extracts all players by team and creates
# panda dataframes specific to each team, afterwhich it writes each
# dataframe to its own CSV and saves it to the local drive in the same
# folder where the script resides. Thus, the analyst can conduct team-
# specific analysis with ease.

import pandas as pd

#Windows filepaths
corepath = '*'
filepath1 = corepath + '*'
filepath2 = corepath + '*'

#Read the raw CSV into the main dataframe
data = pd.read_csv(filepath1 + 'nba_data_processed.csv')

#Set the main dataframe option to print out all columns when we print
#out for checks. Personal preference, not required
pd.set_option('display.max_columns', None)

#Create Team sets and lists
team_name_st = set(data['Tm'].tolist())
team_name_lst = list(team_name_st)

#Create Position sets and lists
position_name_st = set(data['Pos'].tolist())
position_name_lst = list(position_name_st)

#Loop through the list of each Team and extract each player with
#his respective stats with which to create team-specific dataframes
#Write each of these dataframes to its own CSV at the end of each loop
for x in range(len(team_name_lst)):
	x_df = data[(data['Tm'] == team_name_lst[x])]
	x_df.to_csv(filepath2+f'/nba_separated_{team_name_lst[x]}.csv')

#Loop through the list of each Position and extract each player with
#his respective stats with which to create team-specific dataframes
#Write each of these dataframes to its own CSV at the end of each loop
for x in range(len(position_name_lst)):
	x_df = data[(data['Pos'] == position_name_lst[x])]
	x_df.to_csv(filepath2+f'/nba_separated_{position_name_lst[x]}.csv')
