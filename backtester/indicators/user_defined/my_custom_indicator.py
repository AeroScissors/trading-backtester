# backtester/indicators/user_defined/my_custom_indicator.py

from backtester.indicators.base import IndicatorBase

class CustomMA(IndicatorBase):
    name = "CustomMA"

    def compute(self, data):
        w = self.params.get('window', 10)
        return data.ewm(span=w).mean()
