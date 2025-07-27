import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# Ensure the backtester package is discoverable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backtester.indicators import registry

def main():
    print("== Indicator Library Test Script ==")

    # Load real price data from CSV
    csv_path = r"C:\Users\Ignee\OneDrive\Desktop\trading-backtester\data\cleaned_csv_data.csv"
    df = pd.read_csv(csv_path)
    prices = df["close"]  # Use your column name here

    print("\nRegistering user-defined indicators...")
    user_indicator_path = os.path.join(
        os.path.dirname(__file__), '..',
        'backtester', 'indicators', 'user_defined', 'my_custom_indicator.py'
    )
    user_indicator_path = os.path.abspath(user_indicator_path)
    try:
        custom_name = registry.load_user_indicator(user_indicator_path)
        print(f"Registered custom indicator: {custom_name}")
    except Exception as e:
        print("Failed to register custom indicator:", e)
        return

    # Test Built-In SMA
    print("\nTesting built-in SMA...")
    try:
        SMA = registry.get_indicator('SMA')
        sma = SMA(window=5)
        sma_values = sma.compute(prices)
        print("SMA output (last 5):")
        print(sma_values.tail())
    except Exception as e:
        print("SMA test failed:", e)

    # Test User-Defined CustomMA
    print("\nTesting user-defined CustomMA...")
    try:
        CustomMA = registry.get_indicator('CustomMA')
        custom_ma = CustomMA(window=5)
        custom_ma_values = custom_ma.compute(prices)
        print("CustomMA output (last 5):")
        print(custom_ma_values.tail())
    except Exception as e:
        print("CustomMA test failed:", e)

    # Visualization
    print("\nPlotting results...")
    plt.figure(figsize=(10, 5))
    plt.plot(prices, label='Price', linewidth=2)
    if 'sma_values' in locals():
        plt.plot(sma_values, label='SMA(5)')
    if 'custom_ma_values' in locals():
        plt.plot(custom_ma_values, label='CustomMA(5)')
    plt.legend()
    plt.title('Indicator Outputs Test')
    plt.show()

if __name__ == "__main__":
    main()
