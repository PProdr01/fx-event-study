import os
import pandas as pd

OUT_PATH = "data/reference/us_cpi_events.csv"
FRED_CPI_CSV_URL = (
    "https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL"
)

def fetch_cpi_release_dates(start="2015-01-01", end="2025-12-31"):
    """
    Fetch CPI dates from FRED CSV endpoint.
    Uses CPI observation dates as event dates.
    """

    df = pd.read_csv(FRED_CPI_CSV_URL)
    df.columns = ["event_date", "cpi_value"]

    df["event_date"] = pd.to_datetime(df["event_date"])
    df = df[(df["event_date"] >= start) & (df["event_date"] <= end)]

    df["event_name"] = "US CPI"
    df["source"] = "FRED (CPIAUCSL CSV)"

    return df[["event_date", "event_name", "source"]]


def main():
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    events = fetch_cpi_release_dates()
    events.to_csv(OUT_PATH, index=False)
    print(f"Saved {len(events)} CPI events to {OUT_PATH}")
    print(events.head())


if __name__ == "__main__":
    main()
