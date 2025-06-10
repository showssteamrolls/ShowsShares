import yfinance as yf
import os

def fetch_data(tickers=["SPY","VFIAX"]):
    base = os.path.dirname(os.path.dirname(__file__))
    for t in tickers:
        out = os.path.join(base, "data_raw", f"{t.lower()}_data.csv")
        data = yf.Ticker(t).history(period="max")
        data.to_csv(out)
        print(f"Saved {t} data to {out}")

if __name__=="__main__":
    fetch_data()
