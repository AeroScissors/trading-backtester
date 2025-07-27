class DataHandler:
    def __init__(self, connector):
        self.connector = connector
        self.data = None

    def load(self):
        self.data = self.connector.load()

    def check_integrity(self):
        required = {'open', 'high', 'low', 'close', 'volume'}
        cols = {col.lower() for col in self.data.columns}
        if not required.issubset(cols):
            raise ValueError(f"Data missing columns: {required - cols}")

    def clean(self):
        # Example cleaning: drop duplicates, sort by index (date), etc.
        self.data = self.data[~self.data.index.duplicated(keep='first')]
        self.data.sort_index(inplace=True)

    def resample(self, rule='D'):
        # Resample to daily by default; adjust as needed
        ohlc_dict = {
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'volume': 'sum'
        }
        self.data = self.data.resample(rule).apply(ohlc_dict).dropna()

    def save(self, filepath):
        self.data.to_csv(filepath)
