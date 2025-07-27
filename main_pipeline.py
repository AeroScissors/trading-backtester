import os
import pandas as pd

from backtester.data.connectors.csv_connector import CSVConnector
from backtester.data.connectors.yfinance_connector import YFinanceConnector
from backtester.data.data_handler import DataHandler

from backtester.indicators import registry
from backtester.strategy import STRATEGIES
from backtester.backtester_engine import BacktesterEngine
from backtester.results.trade_logger import TradeLogger
from backtester.results.metrics import (
    calculate_sharpe_ratio, calculate_max_drawdown,
    calculate_annualized_return, calculate_volatility, calculate_win_loss
)
from backtester.results.report import export_metrics_csv, generate_summary_pdf

# ============ Utility Functions ============

def load_and_clean_data(
    data_type='csv',
    file_path=None,
    ticker=None,
    start_date=None,
    end_date=None,
    out_path=None
):
    if data_type == 'csv':
        connector = CSVConnector(file_path)
    elif data_type == 'yfinance':
        connector = YFinanceConnector(ticker, start_date, end_date)
    else:
        raise ValueError("Unsupported data_type. Use 'csv' or 'yfinance'.")
    handler = DataHandler(connector)
    handler.load()
    handler.check_integrity()
    handler.clean()
    handler.resample('D')
    handler.save(out_path)
    return out_path

def register_all_indicators():
    # Add custom indicator registration if any
    # registry.load_user_indicator('path/to/my_custom_indicator.py')
    pass

def run_strategy(
    data_path,
    strategy_name='moving_average_crossover',
    short_window=10,
    long_window=30,
    initial_capital=10000,
    results_path=None
):
    os.makedirs(results_path, exist_ok=True)
    data = pd.read_csv(data_path, parse_dates=['date'], index_col='date')
    strategy_class = STRATEGIES[strategy_name]
    strategy = strategy_class(short_window=short_window, long_window=long_window, initial_capital=initial_capital)
    engine = BacktesterEngine(strategy, data)
    trades = engine.run()
    trades_csv_path = os.path.join(results_path, 'trades.csv')
    logger = TradeLogger(trades_csv_path)
    logger.log(trades)
    return trades, data, trades_csv_path

def generate_metrics_and_report(
    data,
    trades,
    results_path=None
):
    returns = data['close'].pct_change().fillna(0)
    equity_curve = (1 + returns).cumprod() * 100
    metrics_dict = {
        "sharpe_ratio": round(calculate_sharpe_ratio(returns), 4),
        "max_drawdown": round(calculate_max_drawdown(equity_curve), 4),
        "annualized_return": round(calculate_annualized_return(equity_curve), 4),
        "volatility": round(calculate_volatility(returns), 4),
        **calculate_win_loss(trades),
    }
    metrics_csv = os.path.join(results_path, "metrics.csv")
    export_metrics_csv(metrics_dict, metrics_csv)
    # generate_summary_pdf(metrics_dict, [...], os.path.join(results_path, "report.pdf"))  # Uncomment and implement if needed
    return metrics_dict, metrics_csv

# ============ Pipeline Entry Function ============

def run_pipeline(input_data):
    """
    Pipeline entrypoint for backend integration
    Expects input_data dict with keys
        data_type, file_path/ticker/start_date/end_date, 
        strategy_name, short_window, long_window, initial_capital, results_path
    """
    # Assign defaults/fetch parameters
    data_type = input_data.get("data_type", "csv")
    file_path = input_data.get("file_path")
    ticker = input_data.get("ticker")
    start_date = input_data.get("start_date")
    end_date = input_data.get("end_date")
    out_path = input_data.get("out_path", "cleaned_csv_data.csv")

    strategy_name = input_data.get("strategy_name", "moving_average_crossover")
    short_window = input_data.get("short_window", 10)
    long_window = input_data.get("long_window", 30)
    initial_capital = input_data.get("initial_capital", 10000)
    results_path = input_data.get("results_path", "results")

    # 1. Prepare Data
    cleaned_csv = load_and_clean_data(
        data_type=data_type,
        file_path=file_path,
        ticker=ticker,
        start_date=start_date,
        end_date=end_date,
        out_path=out_path
    )

    # 2. Register Indicators (optional)
    register_all_indicators()

    # 3. Run strategy
    trades, data, trades_csv_path = run_strategy(
        data_path=cleaned_csv,
        strategy_name=strategy_name,
        short_window=short_window,
        long_window=long_window,
        initial_capital=initial_capital,
        results_path=results_path
    )

    # 4. Generate metrics/report
    metrics_dict, metrics_csv = generate_metrics_and_report(
        data, trades, results_path=results_path
    )

    result = {
        "metrics": metrics_dict,
        "trades_csv": trades_csv_path,
        "metrics_csv": metrics_csv,
        # "pdf_report_path": os.path.join(results_path, "report.pdf")  # Enable if implemented
    }
    return result

# ============ CLI Entrypoint ============

if __name__ == "__main__":
    # Edit these paths for your data/files
    input_csv = r'C:\Users\Ignee\OneDrive\Desktop\trading-backtester\data\reliance_candles.csv'
    cleaned_csv = r'C:\Users\Ignee\OneDrive\Desktop\trading-backtester\data\cleaned_csv_data.csv'
    results_dir = r'C:\Users\Ignee\OneDrive\Desktop\trading-backtester\results'

    # Step 1: Prepare data
    data_csv = load_and_clean_data(
        data_type='csv',
        file_path=input_csv,
        out_path=cleaned_csv
    )
    # Step 2: Register indicators (optional)
    register_all_indicators()
    # Step 3: Run strategy
    trades, data, trades_csv_path = run_strategy(data_csv, results_path=results_dir)
    # Step 4: Generate metrics/report
    metrics, metrics_csv = generate_metrics_and_report(data, trades, results_path=results_dir)
    print("Pipeline complete. Metrics:", metrics)
