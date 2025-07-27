from backtester.data.connectors.csv_connector import CSVConnector
from backtester.data.connectors.yfinance_connector import YFinanceConnector
from backtester.data.data_handler import DataHandler

# CSV Test - use the REAL file you have!
csv_connector = CSVConnector('data/reliance_candles.csv.csv')  # <--- changed this line
csv_handler = DataHandler(csv_connector)
csv_handler.load()
csv_handler.check_integrity()
csv_handler.clean()
csv_handler.resample('D')
csv_handler.save('data/cleaned_csv_data.csv')

# Yahoo Finance Test
yf_connector = YFinanceConnector('AAPL', '2020-01-01', '2020-12-31')
yf_handler = DataHandler(yf_connector)
yf_handler.load()
yf_handler.check_integrity()
yf_handler.clean()
yf_handler.resample('D')
yf_handler.save('data/cleaned_yf_data.csv')
