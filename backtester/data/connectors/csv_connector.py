import pandas as pd

class CSVConnector:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        df = pd.read_csv(
            self.filepath, 
            index_col=0,
            parse_dates=[0],
            dayfirst=True           # because format is 'dd-mm-yyyy HH:MM'
        )
        df.index.name = 'date'
        df.columns = [col.lower() for col in df.columns]  # Standardize columns
        return df
