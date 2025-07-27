import itertools
import pandas as pd

class GridSearchOptimizer:
    def __init__(self, strategy_cls, param_grid, data, metrics_fn):
        self.strategy_cls = strategy_cls
        self.param_grid = param_grid
        self.data = data
        self.metrics_fn = metrics_fn
        self.results = []

    def run(self):
        keys = list(self.param_grid.keys())
        values = list(self.param_grid.values())
        for param_tuple in itertools.product(*values):
            params = dict(zip(keys, param_tuple))
            strategy = self.strategy_cls(**params)
            pnl = strategy.backtest(self.data)
            metrics = self.metrics_fn(pnl)
            self.results.append({**params, **metrics})
        return pd.DataFrame(self.results)

    def save_results(self, filename):
        df = pd.DataFrame(self.results)
        df.to_csv(filename, index=False)
