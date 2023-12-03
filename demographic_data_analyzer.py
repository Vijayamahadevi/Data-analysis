import pandas as pd

df = pd.read_csv('dataset.csv')

#1
race_counts = df['race'].value_counts()

#2
average_age_men = df[df['sex'] == 'Male']['age'].mean()

#3
percentage_bachelors = (df['education'] == 'Bachelors').sum() / len(df) * 100

#4
higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
percentage_higher_education_rich = (df[higher_education]['salary'] == '>50K').sum() / len(df[higher_education]) * 100

#5
lower_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
percentage_lower_education_rich = (df[lower_education]['salary'] == '>50K').sum() / len(df[lower_education]) * 100

#6
min_work_hours = df['hours-per-week'].min()

#7
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_percentage = (num_min_workers['salary'] == '>50K').sum() / len(num_min_workers) * 100

#8
highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
highest_earning_country_percentage = (df[(df['native-country'] == highest_earning_country) & (df['salary'] == '>50K')].shape[0] / df[df['native-country'] == highest_earning_country].shape[0]) * 100

#9
indian_occupation_stats = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts()
top_IN_occupation = indian_occupation_stats.idxmax()

