import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------- core helpers (self-contained) ----------
def load_and_clean(df: pd.DataFrame) -> pd.DataFrame:
    required = ["date", "open", "high", "low", "close", "volume"]
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    for c in ["open", "high", "low", "close", "volume"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna(subset=required)
    df = df.drop_duplicates(subset=["date"]).sort_values("date").reset_index(drop=True)
    return df

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["daily_return"] = out["close"].pct_change()
    out["sma_20"] = out["close"].rolling(20, min_periods=1).mean()
    out["sma_50"] = out["close"].rolling(50, min_periods=1).mean()
    out["ema_12"] = out["close"].ewm(span=12, adjust=False).mean()
    out["ema_26"] = out["close"].ewm(span=26, adjust=False).mean()
    out["volatility_30d"] = out["daily_return"].rolling(30, min_periods=1).std()
    delta = out["close"].diff()
    gain = np.where(delta > 0, delta, 0.0)
    loss = np.where(delta < 0, -delta, 0.0)
    roll_up = pd.Series(gain).rolling(14, min_periods=14).mean()
    roll_down = pd.Series(loss).rolling(14, min_periods=14).mean()
    rs = roll_up / (roll_down.replace(0, np.nan))
    out["rsi_14"] = 100 - (100 / (1 + rs))
    return out

def export_daily_summary(df: pd.DataFrame, filename: str) -> None:
    cols = ["date", "close", "daily_return", "sma_20", "sma_50", "volatility_30d", "rsi_14"]
    df[cols].to_csv(filename, index=False)

def plot_price_with_ma(df: pd.DataFrame, filename: str) -> None:
    fig = plt.figure(figsize=(10, 5))
    plt.plot(df["date"], df["close"], label="Close")
    plt.plot(df["date"], df["sma_20"], label="SMA 20")
    plt.plot(df["date"], df["sma_50"], label="SMA 50")
    plt.title("AAPL Close vs. MA (20/50)")
    plt.xlabel("Date"); plt.ylabel("Price"); plt.legend(); plt.tight_layout()
    fig.savefig(filename, dpi=180); plt.close(fig)

def plot_return_hist(df: pd.DataFrame, filename: str) -> None:
    fig = plt.figure(figsize=(6, 4))
    df["daily_return"].dropna().hist(bins=50)
    plt.title("AAPL Daily Return Distribution")
    plt.xlabel("Daily Return"); plt.ylabel("Frequency"); plt.tight_layout()
    fig.savefig(filename, dpi=180); plt.close(fig)

def plot_volatility(df: pd.DataFrame, filename: str) -> None:
    fig = plt.figure(figsize=(10, 4))
    plt.plot(df["date"], df["volatility_30d"])
    plt.title("AAPL 30D Rolling Volatility (Std of Returns)")
    plt.xlabel("Date"); plt.ylabel("Volatility (30D)"); plt.tight_layout()
    fig.savefig(filename, dpi=180); plt.close(fig)

# ---------- script entry (no external imports, no paths beyond filenames) ----------
if __name__ == "__main__":
    # Read your raw CSV where the first column is the date index (as in your file)
    raw = pd.read_csv("apple_stock.csv", index_col=0, parse_dates=True)
    raw = raw.reset_index().rename(columns={"index": "date"})
    raw.columns = [c.strip().lower().replace(" ", "_") for c in raw.columns]

    clean = load_and_clean(raw)
    clean.to_csv("clean_apple_stock.csv", index=False)

    enriched = add_indicators(clean)
    export_daily_summary(enriched, "apple_sql_daily_summary.csv")
    plot_price_with_ma(enriched, "price_with_ma.png")
    plot_return_hist(enriched, "daily_return_hist.png")
    plot_volatility(enriched, "volatility_trend.png")