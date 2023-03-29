import matplotlib.pyplot as plt
import pandas as pd

#Windows filepaths
corepath = 'C:\\Users\\taylo\\OneDrive\\Documents\\Python_Scripts'
filepath1 = corepath + '\\thisismystuff\\Matplotlib Stuff\\'
filepath2 = corepath + '\\thisismystuff\\Matplotlib Stuff\\NBA Separated CSVs\\'

#Input three-letter Team code
team = input('Team: ')

#Read respective separated CSV determined by user input
data = pd.read_csv(filepath2 + f'nba_separated_{team}.csv')

#Construct lists based upon Player and PTS extracted from
#the CSV read into the 'data' variable above
x = data['Player'].tolist()
y = data['PTS'].tolist()

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
#readability
barplot = plt.barh(x, y,color = '#ee6730')
plt.bar_label(barplot, labels = y, label_type = 'edge')
plt.grid(axis = 'x', linestyle = '--',alpha=0.5)
plt.title(f'{team} Players Ranked by PTS')
plt.yticks(fontsize = 8)
plt.show()