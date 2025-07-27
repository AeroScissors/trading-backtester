import pandas as pd

class BacktesterEngine:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data

    def run(self):
        signals = self.strategy.generate_signals(self.data)
        for signal in signals:
            idx = signal['index']
            action = signal['action']
            price = self.data['close'].iloc[idx]
            date = self.data.index[idx]
            if action == 'BUY' and self.strategy.cash >= price:
                qty = self.strategy.position_size(price)
                self.strategy.cash -= qty * price
                self.strategy.position += qty
                self.strategy.record_trade(date, 'BUY', price, qty)
            elif action == 'SELL' and self.strategy.position > 0:
                qty = self.strategy.position
                self.strategy.cash += qty * price
                self.strategy.position = 0
                self.strategy.record_trade(date, 'SELL', price, qty)
        return self.strategy.trades
