import pandas as pd
from backtester.strategy.base_strategy import BaseStrategy

class MyStrategy(BaseStrategy):
    def __init__(self, sma_short=5, sma_long=20, initial_capital=10000):
        super().__init__(initial_capital)
        self.sma_short = sma_short
        self.sma_long = sma_long

    def generate_signals(self, data):
        """
        Simple moving average crossover strategy:
        Buy when short SMA crosses above long SMA,
        Sell when short SMA crosses below long SMA.
        """
        df = data.copy()
        df['sma_short'] = df['close'].rolling(self.sma_short).mean()
        df['sma_long'] = df['close'].rolling(self.sma_long).mean()
        df.dropna(inplace=True)

        signals = []

        prev_signal = None
        for i in range(1, len(df)):
            prev_short = df['sma_short'].iloc[i - 1]
            prev_long = df['sma_long'].iloc[i - 1]
            curr_short = df['sma_short'].iloc[i]
            curr_long = df['sma_long'].iloc[i]

            # Detect crossover
            if prev_short <= prev_long and curr_short > curr_long:
                signals.append({'index': df.index[i], 'action': 'buy'})
                prev_signal = 'buy'
            elif prev_short >= prev_long and curr_short < curr_long:
                signals.append({'index': df.index[i], 'action': 'sell'})
                prev_signal = 'sell'
            else:
                # no signal
                pass

        return signals
