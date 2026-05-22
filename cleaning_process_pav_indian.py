import pandas as pd
import csv

df = pd.read_csv('indian_developer_burnout_2026.csv')

#print(df.head())

# check for empty rows/ missing values


# check for duplicates
df.info()
missing_values_count = df.isnull().sum() # obtain the of missing data points per column
# look at the of missing points in all columns
print(missing_values_count[:])


print(df['developer_id'].nunique())

print(sum(df.duplicated()))

