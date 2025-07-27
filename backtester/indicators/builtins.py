# backtester/indicators/builtins.py

import pandas as pd
from .base import IndicatorBase

class SMA(IndicatorBase):
    name = "SMA"

    def compute(self, data):
        window = self.params.get('window', 14)
        return data.rolling(window=window).mean()

class RSI(IndicatorBase):
    name = "RSI"

    def compute(self, data):
        window = self.params.get('window', 14)
        delta = data.diff()
        up = delta.clip(lower=0)
        down = -1 * delta.clip(upper=0)
        ma_up = up.rolling(window=window).mean()
        ma_down = down.rolling(window=window).mean()
        rs = ma_up / ma_down
        return 100 - (100 / (1 + rs))
