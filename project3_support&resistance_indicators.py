import pandas as pd
import numpy as np
import talib
import yfinance as yf
import matplotlib.pyplot as plt

# Define function to calculate support and resistance levels
def calculate_support_resistance(symbol):
    # Fetch historical price data
    data = yf.download(symbol, start='2022-01-01', end='2022-12-31')

    # Calculate moving averages
    data['50MA'] = talib.SMA(data['Close'], timeperiod=50)
    data['200MA'] = talib.SMA(data['Close'], timeperiod=200)

    # Identify support and resistance levels
    support_level = data['50MA'].min()
    resistance_level = data['50MA'].max()

    # Plotting support and resistance levels
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close')
    plt.plot(data['50MA'], label='50-day MA')
    plt.plot(data['200MA'], label='200-day MA')
    plt.axhline(y=support_level, color='g', linestyle='--', label='Support')
    plt.axhline(y=resistance_level, color='r', linestyle='--', label='Resistance')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'{symbol} - Support and Resistance Levels')
    plt.legend()
    plt.show()

    return support_level, resistance_level

# Example usage
symbol = 'AAPL'
support, resistance = calculate_support_resistance(symbol)
print(f'Support Level: {support}')
print(f'Resistance Level: {resistance}')
