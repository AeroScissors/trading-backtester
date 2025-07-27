import yfinance as yf
import pandas as pd

class YFinanceConnector:
    def __init__(self, ticker, start, end):
        self.ticker = ticker
        self.start = start
        self.end = end

    def load(self):
        df = yf.download(
            self.ticker,
            start=self.start,
            end=self.end,
            auto_adjust=False
        )
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [str(col[0]).lower() for col in df.columns]
        else:
            df.columns = [str(col).lower() for col in df.columns]

        # Standardizing column names to match your system
        rename_dict = {
            'open': 'open',
            'high': 'high',
            'low': 'low',
            'close': 'close',
            'volume': 'volume'
        }
        df = df.rename(columns=rename_dict)
        df.index.name = 'date'
        return df
