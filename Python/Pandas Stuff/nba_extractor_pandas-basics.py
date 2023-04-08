# This script operates on the 'NBA Player Performance Stats'
# dataset from Kaggle by building a queryable structure for
# the individuals data points by team, indexed by player.
#
# https://www.kaggle.com/datasets/iabdulw/nba-player-performance-stats
#
# The intent of this script is to:
# 1. Work off of the 'nba_data_processed.csv' file in the repository
# 2. Read the raw CSV into a dataframe
# 3. Create lists from the 'Tm' and 'Pos' columns of that dataframe
# 4. Dedupe these lists by converting them to sets temporarily
# 5. Using a for loop, extract each player and his respective stats
#    and create Team or Position-specific dataframes
# 6. Write these new dataframes to CSVs for further analysis
#
# Of note, there are many dynamically-created CSVs as a result of
# this script, so it is important to keep them organized locally
# however you see fit.

import pandas as pd

corepath = '/Users/ifhpclothing/Documents'
filepath = corepath + '/Python_Scripts/NBA Separated CSVs'

#Read the raw CSV into the main dataframe
data = pd.read_csv('nba_data_processed.csv')

#Set the main dataframe option to print out all columns when we print
#out for checks. Personal preference, not required
pd.set_option('display.max_columns', None)

#Create Team sets and lists
team_name_lst = list(set(data['Tm'].tolist()))

#Create Position sets and lists
position_name_lst = list(set(data['Pos'].tolist()))

#Loop through the list of each Team and extract each player with
#his respective stats with which to create team-specific dataframes
#Write each of these dataframes to its own CSV at the end of each loop
for x in range(len(team_name_lst)):
	x_df = data[(data['Tm'] == team_name_lst[x])]
	x_df.to_csv(filepath+f'/nba_separated_{team_name_lst[x]}.csv')

#Loop through the list of each Position and extract each player with
#his respective stats with which to create position-specific dataframes
#Write each of these dataframes to its own CSV at the end of each loop
for x in range(len(position_name_lst)):
	x_df = data[(data['Pos'] == position_name_lst[x])]
	x_df.to_csv(filepath+f'/nba_separated_{position_name_lst[x]}.csv')
