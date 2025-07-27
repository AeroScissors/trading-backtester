import matplotlib.pyplot as plt
import os

def plot_equity_curve(equity_curve, save_path=None):
    plt.figure(figsize=(10, 4))
    plt.plot(equity_curve, label="Equity Curve", color='blue')
    plt.xlabel("Time")
    plt.ylabel("Equity")
    plt.title("Equity Curve")
    plt.legend()
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        plt.close()
    else:
        plt.show()

def plot_trade_marks(price_series, trades, save_path=None):
    plt.figure(figsize=(10, 4))
    plt.plot(price_series, label="Price", color='black')
    for trade in trades:
        entry_idx = trade['entry']
        exit_idx = trade['exit']
        plt.plot(entry_idx, price_series[entry_idx], 'g^', label='Entry' if trade == trades[0] else "")
        plt.plot(exit_idx, price_series[exit_idx], 'rv', label='Exit' if trade == trades[0] else "")
    plt.title("Trades on Price Chart")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        plt.close()
    else:
        plt.show()

def save_chart(fig, filename):
    fig.savefig(filename, bbox_inches='tight')
