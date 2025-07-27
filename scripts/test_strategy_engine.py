import os
import pandas as pd
from backtester.strategy import STRATEGIES
from backtester.backtester_engine import BacktesterEngine
from backtester.results.trade_logger import TradeLogger

# === ENSURE RESULTS DIRECTORY EXISTS ===
os.makedirs('results', exist_ok=True)

# === LOAD CLEANED DATA ===
data = pd.read_csv('data/cleaned_csv_data.csv', parse_dates=['date'], index_col='date')

# Check columns (optional, helps debug casing issues)
expected_cols = {'open', 'high', 'low', 'close', 'volume'}
actual_cols = set(data.columns.str.lower())
if not expected_cols.issubset(actual_cols):
    print(f"Warning: Missing expected columns: {expected_cols - actual_cols}")
    print(f"Found columns: {data.columns}")

# === INSTANTIATE STRATEGY ===
strategy_class = STRATEGIES["moving_average_crossover"]
# You can customize short/long windows here
strategy = strategy_class(short_window=10, long_window=30, initial_capital=10000)

# === RUN BACKTEST ===
engine = BacktesterEngine(strategy, data)
trades = engine.run()

# === LOG TRADES ===
logger = TradeLogger('results/test_trades.csv')
logger.log(trades)

# === PRINT SUMMARY ===
print(f"Total Trades: {len(trades)}")
if trades:
    for trade in trades:
        print(trade)
else:
    print("No trades executed. Check your strategy parameters or ensure data contains some crossovers.")
