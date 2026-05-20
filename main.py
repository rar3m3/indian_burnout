import pandas as pd
import numpy as np

#import data csv
df = pd.read_csv('indian_developer_burnout_2026.csv')
print(df.info())

#ducplicate check (only for id, because reasons)
print(sum(df.duplicated(subset=['developer_id'])))

#function to replace missing numeric values with average if no zeros, else with zeros
def replace_nulls(df, column):                    
    zero_count = (df[column] == 0).sum()
    if zero_count > 0:               
        mean_value = df[column].mean(skipna=True)     
        df[column] = df[column].fillna(mean_value)
    else:                                             
        df[column] = df[column].fillna(0)

#apply function to needed columns
replace_nulls(df,'upskilling_hours_per_week')
replace_nulls(df,'leetcode_problems_solved')
replace_nulls(df,'certifications_count')
replace_nulls(df,'side_projects_count')
replace_nulls(df,'github_activity_score')
replace_nulls(df,'interview_preparation_hours_weekly')
replace_nulls(df,'caffeine_intake_per_day')
replace_nulls(df,'social_media_usage_hours')
replace_nulls(df,'emergency_savings_months')
replace_nulls(df,'linkedin_job_search_activity')

#replace nulls for 'therapy_or_counseling'
df['therapy_or_counseling'] = df['therapy_or_counseling'].fillna('NA')

#recheck for nulls
na_counts = df.isna().sum()
print(na_counts)


