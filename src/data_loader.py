import os

import numpy as np
import pandas as pd
import yfinance as yf

PAIR = "EURUSD=X" # Yahoo Finance ticket for EUR/USD Pair
START = "2015-01-01"
END = "2025-12-31"

RAW_DIR = "data/raw/"
os.makedirs(RAW_DIR, exist_ok=True)

def download_fx_prices(ticker=PAIR, start=START, end=END) -> pd.DataFrame:
    df = yf.download(ticker, start=start, end=end, auto_adjust=False, progress=False)
    if df.empty:
        raise ValueError("No data returned from yfinance. Check internet connection or ticker symbol.")

    # If yfinance returns MultiIndex Columns, drop the second level
    # Example column becomes ("Close", "EURUSD=X") -> "Close"
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.reset_index()

    # Standardize Column Names
    df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]

    # Some yfinance Outputs don't Include Volume for FX
    expected = ["date", "open", "high", "low", "close", "adj_close", "volume"]
    for col in expected:
        if col not in df.columns:
            df[col] = pd.NA
    df = df[expected]
    return df

def main():
    prices = download_fx_prices()
    out_path = os.path.join(RAW_DIR, "eurusd_daily.csv")
    prices.to_csv(out_path, index=False)
    print(f"Saved {len(prices)} rows to {out_path}")
    print(prices.head())

if __name__ == "__main__":
    main()