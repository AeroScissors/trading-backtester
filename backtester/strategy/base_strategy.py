from abc import ABC, abstractmethod
import pandas as pd

class BaseStrategy(ABC):
    def __init__(self, initial_capital=10000):
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.position = 0
        self.trades = []  # Log of trades

    @abstractmethod
    def generate_signals(self, data):
        """
        Abstract method: Implement logic for buy/sell signals.

        Should return a list of dicts, each dict containing:
        {
            'index': int or label (e.g., timestamp),
            'action': 'buy' or 'sell',
            'quantity': int (optional)
        }
        """
        pass

    def position_size(self, price):
        """
        Calculate the position size to buy based on current cash.
        Default: invest all available cash.
        """
        return int(self.cash // price)

    def record_trade(self, date, action, price, quantity):
        """
        Record a trade in the trades log with current cash and position.
        Accepts 'buy'/'sell' in any case (e.g. 'BUY', 'Buy', 'buy').
        """
        action = action.lower()
        if action == 'buy':
            cost = price * quantity
            self.cash -= cost
            self.position += quantity
        elif action == 'sell':
            proceeds = price * quantity
            self.cash += proceeds
            self.position -= quantity
        else:
            raise ValueError(f"Unknown action '{action}'")

        self.trades.append({
            "date": date,
            "action": action,
            "price": price,
            "quantity": quantity,
            "cash": self.cash,
            "position": self.position
        })

    def backtest(self, data):
        """
        Runs signal generation and applies trades; returns portfolio equity curve.

        Args:
            data (pd.DataFrame): Market data with at least 'close' prices and index (datetime or int).

        Returns:
            pd.Series: equity curve indexed by the same index type as signals.
        """
        signals = self.generate_signals(data)
        equity = []
        for signal in signals:
            idx = signal['index']  # label (datetime/int)
            action = signal['action']
            quantity = signal.get('quantity')
            price = data.loc[idx, 'close']
            date = idx

            if quantity is None:
                quantity = self.position_size(price)

            self.record_trade(date, action, price, quantity)
            current_value = self.cash + self.position * price
            equity.append(current_value)

        return pd.Series(equity, index=[signal['index'] for signal in signals])
