# pipeline.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_charts(clean_csv: str):
    """
    Generate 3 charts from cleaned Walmart sales data.
    """
    df = pd.read_csv(clean_csv)
    df['week_start'] = pd.to_datetime(df['week_start'])

    # Chart 1: Weekly Total Sales Trend
    chart1 = df.groupby('week_start')['Weekly_Sales'].sum().reset_index()
    plt.figure(figsize=(10,5))
    sns.lineplot(data=chart1, x='week_start', y='Weekly_Sales', marker='o')
    plt.title('Weekly Total Sales Trend')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("chart1_weekly_trend.png")
    plt.close()

    # Chart 2: Store YoY Growth Top 10
    store_yoy = df.groupby('Store')['yoy_growth'].mean().reset_index()
    store_yoy = store_yoy.sort_values('yoy_growth', ascending=False).head(10)
    plt.figure(figsize=(8,5))
    sns.barplot(data=store_yoy, x='yoy_growth', y='Store')
    plt.title('Store YoY Growth Top 10')
    plt.xlabel('Average YoY Growth')
    plt.tight_layout()
    plt.savefig("chart2_store_yoy_top10.png")
    plt.close()

    # Chart 3: Dept Lift vs MA4 Top 20
    df['lift'] = (df['Weekly_Sales'] - df['sales_ma_4']) / df['sales_ma_4']
    dept_lift = df.groupby('Dept')['lift'].mean().reset_index()
    dept_lift = dept_lift.sort_values('lift', ascending=False).head(20)
    plt.figure(figsize=(8,6))
    sns.barplot(data=dept_lift, x='lift', y='Dept')
    plt.title('Dept Lift vs 4-Week MA Top 20')
    plt.xlabel('Average Lift')
    plt.tight_layout()
    plt.savefig("chart3_dept_lift_top20.png")
    plt.close()

    print("Charts saved: chart1_weekly_trend.png, chart2_store_yoy_top10.png, chart3_dept_lift_top20.png")
