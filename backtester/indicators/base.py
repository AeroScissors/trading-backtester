# backtester/indicators/base.py

class IndicatorBase:
    name = "Base"

    def __init__(self, **params):
        self.params = params

    def compute(self, data):
        """
        Compute the indicator on the provided data (e.g., pandas Series/DataFrame).
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Indicator must implement 'compute' method.")

    @classmethod
    def validate_params(cls, params):
        """Optional: Validate parameter types/values."""
        pass
