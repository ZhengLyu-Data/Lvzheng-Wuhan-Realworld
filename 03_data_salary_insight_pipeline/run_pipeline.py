
import pandas as pd
from clean_data import clean_salary_data
from pipeline import process_salary_data

# Load and clean data
input_file = 'data_science_salaries_raw.csv'
df_cleaned = clean_salary_data(input_file)

# Analyze
results = process_salary_data(df_cleaned)

# Show results
print("📊 Avg Salary by Experience Level:")
print(results['salary_by_experience'])

print("\n🏆 Top 10 Salaries by Job Title:")
print(results['top10_salary_by_title'])

print("\n🌍 Top 10 Salaries by Location:")
print(results['top10_salary_by_location'])
