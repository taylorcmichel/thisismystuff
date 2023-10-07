import numpy as np
import pandas as pd

set_length = 100000

# Set seed for reproducibility
# np.random.seed(123)

# Generate fake data for ID
id_data = np.arange(1, set_length + 1)

# Generate fake data for age
age_data = np.random.normal(loc=35, scale=10, size=set_length).astype(int)

# Generate fake data for weight
weight_data = np.random.normal(loc=70, scale=10, size=set_length).round(2)

# Generate fake data for level of education
education_data = np.random.choice(['High school', 'Bachelor', 'Master', 'PhD'], size=set_length)

# Generate fake data for job position
job_data = np.random.choice(['Manager', 'Engineer', 'Analyst', 'Developer', 'Sales', 'Other'], size=set_length)

# Generate fake data for years in current job
years_data = np.random.randint(low=1, high=30, size=set_length)

# Generate fake data for city in Norway
city_data = np.random.choice(['Oslo', 'Bergen', 'Trondheim', 'Stavanger', 'Drammen'], size=set_length)

# Generate fake data for salary
salary_data = np.random.normal(loc=500000, scale=100000, size=set_length).round(2)

# Generate fake data for smoking status
smoking_data = np.random.choice(['Yes', 'No'], size=set_length)

# Create a dictionary of the fake data
data = {'ID': id_data,
        'Age': age_data,
        'Weight': weight_data,
        'Level of Education': education_data,
        'Job Position': job_data,
        'Years in Current Job': years_data,
        'City in Norway': city_data,
        'Salary': salary_data,
        'Smoker': smoking_data}

# Create a pandas dataframe from the dictionary
df = pd.DataFrame(data)

print(df)
