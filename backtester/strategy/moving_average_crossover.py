from .base_strategy import BaseStrategy
import pandas as pd

class MovingAverageCrossoverStrategy(BaseStrategy):
    def __init__(self, short_window=10, long_window=50, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data):
        signals = []
        data['short_ma'] = data['close'].rolling(self.short_window).mean()
        data['long_ma'] = data['close'].rolling(self.long_window).mean()

        for idx in range(1, len(data)):
            if data['short_ma'].iloc[idx-1] < data['long_ma'].iloc[idx-1] and \
               data['short_ma'].iloc[idx] > data['long_ma'].iloc[idx]:
                signals.append({'index': idx, 'action': 'BUY'})
            elif data['short_ma'].iloc[idx-1] > data['long_ma'].iloc[idx-1] and \
                 data['short_ma'].iloc[idx] < data['long_ma'].iloc[idx]:
                signals.append({'index': idx, 'action': 'SELL'})
        return signals
