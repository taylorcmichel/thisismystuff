# This script continues work on the 'NBA Player Performance Stats'
# dataset from Kaggle by building Matplotlib bar charts from
# custom dataframes constructed from the overall raw CSV.
import matplotlib.pyplot as plt
import pandas as pd

#Windows filepaths
corepath = '*'
filepath1 = corepath + '\\*'
filepath2 = filepath1 + '*\\'

#Input three-letter Team code
position = input('Position: ')

#Read respective separated CSV determined by user input
data = pd.read_csv(filepath2 + f'nba_separated_{position}.csv')
new_data = data.head(15)

#Construct lists based upon Player and PTS extracted from
#the CSV read into the 'data' variable above
x = new_data['Player'].tolist()
y = new_data['PTS'].tolist()

#Build a Pandas dataframe containing only the information
#we require for this graph: Players and PTS
df = pd.DataFrame({'Player': x, 'PTS': y})

#Sort the dataframe created above in order to make the graph
#we're about to create easier for the user to digest.
df_sorted = df.sort_values('PTS')

#Extract x and y variables from the dataframe and place
#them in their respective lists
x = df_sorted['Player'].tolist()
y = df_sorted['PTS'].tolist()

#Plot x and y in horizontal bar chart for maximum
#readability and adds PTS value as label on bar edge
barplot = plt.barh(x, y,color = '#ee6730')
plt.bar_label(barplot, labels = y, label_type = 'edge', fontsize = 6)
plt.grid(axis = 'x', linestyle = '--',alpha=0.5)
plt.title(f'{position} Players Ranked by Position by PTS')
plt.yticks(fontsize = 6)
plt.show()
