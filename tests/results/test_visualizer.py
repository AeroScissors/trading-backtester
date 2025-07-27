from backtester.results import visualizer
import numpy as np

def test_plot_equity_curve(tmp_path):
    eq = np.linspace(100, 200, 100)
    out_path = tmp_path / "equity.png"
    visualizer.plot_equity_curve(eq, save_path=str(out_path))
    assert out_path.exists()

def test_plot_trade_marks(tmp_path):
    price = np.linspace(100, 120, 100)
    trades = [{'entry': 10, 'exit': 20}, {'entry': 50, 'exit': 70}]
    out_path = tmp_path / "trades.png"
    visualizer.plot_trade_marks(price, trades, save_path=str(out_path))
    assert out_path.exists()
