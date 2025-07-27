import numpy as np
import random

def calculate_sharpe_ratio(returns, risk_free=0.0):
    returns = np.array(returns)
    excess = returns - risk_free
    std = np.std(excess)
    if std == 0:
        return np.nan
    return np.mean(excess) / std * np.sqrt(252)

def calculate_max_drawdown(equity_curve):
    equity_curve = np.array(equity_curve)
    if equity_curve.size == 0:
        return np.nan
    peak = np.maximum.accumulate(equity_curve)
    drawdown = (equity_curve - peak) / peak
    return np.min(drawdown)

def calculate_annualized_return(equity_curve, periods_per_year=252):
    # Use iloc for Series with non-int index, else fallback to position
    if hasattr(equity_curve, 'iloc'):
        if len(equity_curve) == 0:
            return np.nan
        start_val = equity_curve.iloc[0]
        end_val = equity_curve.iloc[-1]
    else:
        if len(equity_curve) == 0:
            return np.nan
        start_val = equity_curve[0]
        end_val = equity_curve[-1]
    total_return = end_val / start_val - 1
    years = len(equity_curve) / periods_per_year
    if years == 0:
        return np.nan
    return (1 + total_return) ** (1 / years) - 1

def calculate_volatility(returns, periods_per_year=252):
    returns = np.array(returns)
    return np.std(returns) * np.sqrt(periods_per_year)

def calculate_win_loss(trades):
    wins, losses = 0, 0
    win_pnl, loss_pnl = 0, 0
    for trade in trades:
        pnl = trade.get('pnl', 0)
        if pnl >= 0:
            wins += 1
            win_pnl += pnl
        else:
            losses += 1
            loss_pnl += pnl
    total = wins + losses
    return {
        "win_rate": wins / total if total else 0,
        "loss_rate": losses / total if total else 0,
        "avg_win": win_pnl / wins if wins else 0,
        "avg_loss": loss_pnl / losses if losses else 0,
        "total_trades": total
    }

def compute_metrics(equity_curve=None, returns=None, trades=None):
    # Generate dummy data if not provided, for testing
    if equity_curve is None:
        equity_curve = np.cumprod(1 + np.random.normal(0.001, 0.02, 252))
    if returns is None:
        returns = np.random.normal(0.001, 0.02, 252)
    if trades is None:
        trades = [{'pnl': random.gauss(50, 30)} for _ in range(50)]
    # Defensive: check for emptiness
    if len(equity_curve) == 0 or len(returns) == 0:
        return {
            "Sharpe": np.nan,
            "MaxDrawdown": np.nan,
            "AnnReturn": np.nan,
            "Volatility": np.nan,
            "win_rate": 0,
            "loss_rate": 0,
            "avg_win": 0,
            "avg_loss": 0,
            "total_trades": 0
        }
    metrics = {}
    metrics['Sharpe'] = calculate_sharpe_ratio(returns)
    metrics['MaxDrawdown'] = calculate_max_drawdown(equity_curve)
    metrics['AnnReturn'] = calculate_annualized_return(equity_curve)
    metrics['Volatility'] = calculate_volatility(returns)
    metrics.update(calculate_win_loss(trades))
    return metrics

# Example run: see if everything works
if __name__ == "__main__":
    metrics = compute_metrics()
    for key, val in metrics.items():
        print(f"{key}: {val}")
