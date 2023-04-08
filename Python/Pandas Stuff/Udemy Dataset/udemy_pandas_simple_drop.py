# This script operates on a 'Udemy Courses Data 2023' dataset
# from Kaggle that can be downloaded here:
#
# https://www.kaggle.com/datasets/ankushbisht005/udemy-courses-data-2023
#
# The intent of this script is to:
# 1. Work off of the 'instructors.csv' file in the repository
# 2. Delete or 'drop' unnecessary or unwanted columns
# 3. Double check to ensure the remaining columns are those we want
# 
# This method is much more efficient than that depicted in 'udemy_pandas'
# in terms of crafting the end product that we desire from the table
# that we are given.

import pandas as pd

#Filepaths
corepath = '*'
filepath = corepath + '*'

#Set dataframe option to print all columns upon printing
#Personal preference, not required
pd.set_option('display.max_columns', None)

#Read raw CSV into dataframe
df = pd.read_csv(filepath + 'instructors.csv')

#Drop columns indexed at 6 and 7
df.drop(df.columns[[6,7]], axis=1, inplace=True)

#Print a list of the current column headers after the drop to ensure the
#drop affected the correct columns
print(list(df.columns))

#Write the amended dataframe to a new CSV
df.to_csv(filepath + 'instructors_result_drop.csv')
