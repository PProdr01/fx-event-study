# FX Market Event Study: EUR/USD Reaction to US CPI

## Project Overview

This project analyzes how the EUR/USD exchange rate reacts to US CPI (Consumer Price Index) releases focusing on:

- Return behavior around CPI release days
- Volatility dynamics before and after the event
- Statistical comparison of CPI vs non-CPI trading days

---

## Business Question Answered

- Do CPI releases create **abnormal returns** in EUR/USD?
- Is **volatility elevated** around inflation announcements?
- Are CPI days statistically different from normal trading days?
- Does the markets reaction occur before, on, or after the release?

---

## Key Findings (Summary)

- Average EUR/USD returns on CPI days are slightly negative, but not statistically significant at 5% level.
![Average EUR/USD Daily Log Retunrs Around CPI](reports/figures/01_avg_return_cpi_window.png)
- Rolling volatility increases after CPI releases, suggesting post-event repricing rather than an immediate shock.
![EUR/USD Volatility Around CPI](reports/figures/02_volatility_cpi_window.png)
- FX markets appear directionally efficient on CPI days, with volatility effects dominating return effects.
- Results are consistent with how highly liquid FX markets typically absorb macroeconomic information.

> These fundings suggest CPI releases are more relevant for risk management and volatility positioning than for directional daily trading strategies.

For a deeper discussion of the methodology, statistical testing, and business interpretation, see **[ANALYSIS.md](ANALYSIS.md)**.

---

## Methodology (High Level)

1. Download daily EUR/USD price data from yfinance
2. Compute:
    - Daily log returns
    - 20-day rolling annualized volatility
3. Automatically fetch CPI event dates from **FRED**
4. Align CPI dates to FX trading days
5. Build a +-5 trading-day event window
6. Compare:
    - CPI days vs non-CPI days
    - Volatility and returns around the event
7. Run Welch two-sample t-tests

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Download CPI Event Calendar
```bash
py src/load_cpi_calendar.py
```

### 3. Download FX Price Data
```bash
py src/data_loader.py
```

### 4. Run Analysis
Open and run:
```bash
notebooks/01_event_study.ipynb