
import pandas as pd

def process_salary_data(df):
    results = {}

    # Average salary by experience level
    results['salary_by_experience'] = df.groupby('experience_level')['salary_usd'].mean().round(2).sort_values(ascending=False)

    # Average salary by job title (Top 10)
    results['top10_salary_by_title'] = df.groupby('job_title')['salary_usd'].mean().round(2).sort_values(ascending=False).head(10)

    # Average salary by company location (Top 10)
    results['top10_salary_by_location'] = df.groupby('location')['salary_usd'].mean().round(2).sort_values(ascending=False).head(10)

    return results
