import yfinance as yf
import pandas as pd

def get_stock_data(ticker: str, start="2018-01-01", end="2024-01-01") -> pd.Series:
    data = yf.download(ticker, start=start, end=end, progress=False)
    if isinstance(data.columns, pd.MultiIndex):
        return data[("Close", ticker)]
    else:
        return data["Close"]



