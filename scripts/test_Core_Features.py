import os
import numpy as np
import pandas as pd
from backtester.results.metrics import (
    calculate_sharpe_ratio,
    calculate_max_drawdown,
    calculate_annualized_return,
    calculate_volatility,
    calculate_win_loss,
)
from backtester.results.visualizer import plot_equity_curve, plot_trade_marks
from backtester.results.report import export_metrics_csv, generate_summary_pdf

def main():
    # --- Specify your OHLCV file ---
    file_path = r"C:\Users\Ignee\OneDrive\Desktop\trading-backtester\data\cleaned_csv_data.csv"
    # (Rename accordingly: file should have columns: date, open, high, low, close, volume)

    # --- Load and process data ---
    df = pd.read_csv(file_path, parse_dates=['date'])
    # Compute returns from 'close'
    df['returns'] = df['close'].pct_change().fillna(0)
    returns = df['returns'].values
    # Build an equity curve starting at 100
    df['equity_curve'] = (1 + df['returns']).cumprod() * 100
    equity_curve = df['equity_curve'].values
    # Use 'close' as the price series for charting
    price_series = df['close'].values
    # Trades list: empty or create if you have separate trade generation logic
    trades = []

    # --- Output directory ---
    out_dir = os.path.join(os.path.dirname(__file__), "outputs")
    os.makedirs(out_dir, exist_ok=True)

    # --- Compute metrics ---
    metrics_dict = {
        "sharpe_ratio": round(calculate_sharpe_ratio(returns), 4),
        "max_drawdown": round(calculate_max_drawdown(equity_curve), 4),
        "annualized_return": round(calculate_annualized_return(equity_curve), 4),
        "volatility": round(calculate_volatility(returns), 4),
        **calculate_win_loss(trades)
    }
    print("\nCalculated Performance Metrics:")
    for k, v in metrics_dict.items():
        print(f"{k}: {v}")

    # --- Generate charts ---
    eq_curve_img = os.path.join(out_dir, "equity_curve.png")
    trades_img = os.path.join(out_dir, "trade_marks.png")
    plot_equity_curve(equity_curve, save_path=eq_curve_img)
    plot_trade_marks(price_series, trades, save_path=trades_img)
    print(f"\nCharts saved as {eq_curve_img}, {trades_img}")

    # --- Export metrics as CSV ---
    metrics_csv = os.path.join(out_dir, "metrics.csv")
    export_metrics_csv(metrics_dict, metrics_csv)
    print(f"\nMetrics saved as {metrics_csv}")

    # --- Export PDF summary ---
    report_pdf = os.path.join(out_dir, "backtest_report.pdf")
    generate_summary_pdf(metrics_dict, [eq_curve_img, trades_img], report_pdf)
    print(f"\nSummary PDF saved as {report_pdf}")

if __name__ == "__main__":
    main()
