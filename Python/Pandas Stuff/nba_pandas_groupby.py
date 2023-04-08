# This script operates on the 'NBA Player Performance Stats'
# dataset from Kaggle by building a queryable structure for
# the individuals data points by team, indexed by player.
#
# https://www.kaggle.com/datasets/iabdulw/nba-player-performance-stats
#
# The intent of this script is to:
# 1. Work off of the 'nba_data_processed.csv' file in the repository
# 2. Reset the index of the dataset to the 'Player' column
# 3. Create an iterable list of Team 3-letter codes for querying
# 4. Create a While loop for indefinite iteration of core code
# 5. Print unpacked lists of 3-letter NBA Team codes
# 6. Prompt for user input of valid 3-letter NBA Team code
# 7. Print team stats contained in CSV for user-defined query
# 8. Cycle back to 5-7 until 'exit' or 'EXIT' is input by user
# 
# Of note, there is no new CSV created by this script, nor is it
# needed. Only terminal output.

import pandas as pd

#Filepaths
corepath = '*'
filepath = corepath + '*'

#Load dataframe with raw CSV
df = pd.read_csv('nba_data_processed.csv')

#Set dataframe index to 'Player' column
df.set_index('Player', inplace=True)

#Set dataframe option to display maximum columns. Not required,
#personal preference
pd.set_option('display.max_columns', 800)

#Create iterable lists of 3-letter Team codes
tm_lst = list(set(df['Tm'].tolist()))
tm_lst_1 = tm_lst[0:15]
tm_lst_2 = tm_lst[15:31]

#Create while loop for indefinite iteration of core code
op = False
while op == False:

	#Unpack 'tm_lst-1' and 'tm_lst_2'and separate them for
	#readability while printing
	print(*tm_lst_1, sep = ' | ')
	print(*tm_lst_2, sep = ' | ')

	#Prompt user for input
	team = input('Input Team: ').upper()

	#If user input doesn't equal 'EXIT', execute core code
	if team != 'EXIT':

		#Group dataframe by column 'Tm'
		tm_grp = df.groupby(['Tm'])

		#Print each line of data extracted by grouping executed above
		print(tm_grp.get_group(team))

	#If user input does equal 'EXIT', break from While loop, end script
	else:
		break
		
