import numpy as np
from backtester.results import metrics

def test_calculate_sharpe_ratio():
    returns = np.array([0.01, 0.02, -0.01])
    sr = metrics.calculate_sharpe_ratio(returns)
    assert isinstance(sr, float)

def test_calculate_max_drawdown():
    eq = np.array([100, 120, 90, 150, 80])
    dd = metrics.calculate_max_drawdown(eq)
    assert dd <= 0

def test_calculate_annualized_return():
    eq = np.array([100, 105, 110, 120])
    ar = metrics.calculate_annualized_return(eq)
    assert isinstance(ar, float)

def test_calculate_volatility():
    returns = np.random.normal(0, 0.01, size=252)
    vol = metrics.calculate_volatility(returns)
    assert vol > 0

def test_calculate_win_loss():
    trades = [{'pnl': 100}, {'pnl': -20}, {'pnl': 30}]
    wl = metrics.calculate_win_loss(trades)
    assert 'win_rate' in wl and 'loss_rate' in wl
