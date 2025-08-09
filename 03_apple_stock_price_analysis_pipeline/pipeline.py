import pandas as pd
import matplotlib.pyplot as plt

def analyze_stock_data(csv_path: str):
    # Load cleaned stock data
    df = pd.read_csv(csv_path, parse_dates=["date"])
    df = df.sort_values("date")

    # 1. Summary statistics
    summary = df.describe()

    # 2. Plot: Closing price over time
    fig1, ax1 = plt.subplots()
    ax1.plot(df["date"], df["close"], color="blue")
    ax1.set_title("Apple Stock Closing Price Over Time")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Close Price")
    fig1.tight_layout()
    fig1.savefig("plot_close_price.png")

    # 3. Plot: Trading volume over time
    fig2, ax2 = plt.subplots()
    ax2.bar(df["date"], df["volume"], color="orange")
    ax2.set_title("Apple Stock Trading Volume Over Time")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Volume")
    fig2.tight_layout()
    fig2.savefig("plot_volume.png")

    # 4. Plot: High vs Low price spread
    fig3, ax3 = plt.subplots()
    ax3.fill_between(df["date"], df["low"], df["high"], color="lightblue", alpha=0.5)
    ax3.set_title("Daily High-Low Price Range")
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Price")
    fig3.tight_layout()
    fig3.savefig("plot_high_low.png")

    # Save summary statistics
    summary.to_csv("stock_summary.csv")

    return summary, (fig1, fig2, fig3)
