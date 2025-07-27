import pandas as pd

from backtester.strategy.my_strategy import MyStrategy  # use concrete strategy here
from backtester.results.metrics import compute_metrics
from backtester.optimizer.grid_search import GridSearchOptimizer

if __name__ == "__main__":
    data_path = "data/cleaned_csv_data.csv"  # confirm this path exists and file has 'close' column
    data = pd.read_csv(data_path, index_col=0)  # if your CSV has datetime or index column

    param_grid = {
        "sma_short": range(5, 31, 5),
        "sma_long": range(20, 101, 20)
    }

    optimizer = GridSearchOptimizer(
        strategy_cls=MyStrategy,
        param_grid=param_grid,
        data=data,
        metrics_fn=compute_metrics,
    )

    df_results = optimizer.run()
    optimizer.save_results("backtester/results/outputs/grid_search_results.csv")
    best = df_results.sort_values("Sharpe", ascending=False).head(10)
    best.to_csv("backtester/results/outputs/best_params.csv", index=False)
