# This script operates on a 'Udemy Courses Data 2023' dataset
# from Kaggle that can be downloaded here:
#
# https://www.kaggle.com/datasets/ankushbisht005/udemy-courses-data-2023
#
# The intent of this script is to: 
# 1. Deconstruct the 'Instructors' data table
# 2. Create an additional table with pertinent data from the first
# 3. Delete or 'drop' the columns containing references to images
# 4. Reconstruct the original table using the two 'new' tables
# 
# Yes, this is a much more complicated way to get same result that could
# be obtained by simply dropping columns from the original table, but the
# purpose of this script is to help demonstrate my ability to use the
# Pandas library.

import pandas as pd

#Mac filepaths
corepath = '*'
filepath = corepath + '*'

#Set dataframe option to print all columns upon printing
#Personal preference, not required
pd.set_option('display.max_columns', None)

#Read raw CSV into dataframe
df = pd.read_csv(filepath + 'instructors.csv')

#Create lists from columns that will be moved to separate table
instructor_job_title = df['job_title'].tolist()
instructor_initials = df['initials'].tolist()
instructor_url = df['url'].tolist()

#Create new dataframe/table using lists created just above
ndf = pd.DataFrame({'job_title': instructor_job_title,
					'initials': instructor_initials,
					'url': instructor_url})

#Drop above columns plus those with references to images from original
#dataframe/table
df.drop(df.columns[[5, 6, 7, 8, 9]], axis=1, inplace=True)

#Write both dataframes/tables to new CSVs
df.to_csv(filepath + 'instructors_left.csv')
ndf.to_csv(filepath + 'instructors_right.csv')

result = pd.concat([df, ndf], axis=1, join='inner')
result.to_csv(filepath + 'instructors_result.csv')


