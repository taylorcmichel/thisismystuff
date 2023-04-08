# This script operates on a 'Udemy Courses Data 2023' dataset
# from Kaggle that can be downloaded here:
#
# https://www.kaggle.com/datasets/ankushbisht005/udemy-courses-data-2023
#
# The intent of this script is to:
# 1. Work off of the 'courses.csv' file in the repository
# 2. Construct filters based off of columns in the data
# 3. Create a new dataframe based off of these filters
# 4. Write this new dataframe to a new CSV
# 
# This new CSV will isolate a core of information from the greater raw
# dataset that we can that we can further focus on if need be.

import pandas as pd

#Filepaths
corepath = '*'
filepath = corepath + '*'

#Read the raw CSV into a Pandas dataframe
df = pd.read_csv(filepath + 'courses.csv')

#Set the option to display all columns upon printing the dataframe
#Personal preference, not required
pd.set_option('display.max_columns', None)

#Round all 'rating' metrics to two decimal places
df = df.round({'rating':2})

#Create three filters based upon column values. The third filter will
#look for course titles containing the word 'Python'
high_rating = (df['rating'] > 4.5)
high_num_reviews = (df['num_reviews'] > 100000)
python = df['title'].str.contains('Python', na=False)

#Create a new dataframe using the above filters and only the referenced
#columns, leaving all other columns out
ndf = df.loc[high_rating & high_num_reviews & python,
      ['title', 'duration', 'rating', 'num_reviews']]

#Sort by ratings, descending
ndf.sort_values(['rating'], inplace=True, ascending=False)

#Write the new dataframe to a new CSV for further use and/or analysis
ndf.to_csv(filepath + 'courses_filtered_ratings-reviews.csv')


