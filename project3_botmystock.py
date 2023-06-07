import alpaca_trade_api as tradeapi

# Initialize the Alpaca API
api = tradeapi.REST('CKMGDFPR3405MOQJ2OP9', 'CDRbraR9PhRUlWAwEirrwWg0DAXgV64aVcuZuwJO', base_url='https://paper-api.alpaca.markets')  # Use 'https://api.alpaca.markets' for live trading

# Define your trading bot strategy
def trading_strategy():
    # Get market data
    barset = api.get_barset('AAPL', 'day', limit=2)  # Get the last two days of AAPL data
    aapl_bars = barset['AAPL']
    
    # Calculate indicators or perform analysis on the market data
    previous_close = aapl_bars[0].c
    current_close = aapl_bars[1].c
    
    # Implement your trading logic
    if current_close > previous_close:
        # Place a buy order
        api.submit_order(
            symbol='AAPL',
            qty=1,  # Number of shares to buy
            side='buy',
            type='market',
            time_in_force='gtc'
        )
    elif current_close < previous_close:
        # Place a sell order
        api.submit_order(
            symbol='AAPL',
            qty=1,  # Number of shares to sell
            side='sell',
            type='market',
            time_in_force='gtc'
        )

# Run the trading bot
trading_strategy()
