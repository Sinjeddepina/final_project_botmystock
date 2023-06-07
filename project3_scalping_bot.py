import alpaca_trade_api as tradeapi

# Initialize the Alpaca API
api = tradeapi.REST('CKMGDFPR3405MOQJ2OP9', 'CDRbraR9PhRUlWAwEirrwWg0DAXgV64aVcuZuwJO', base_url='https://paper-api.alpaca.markets')  # Use 'https://api.alpaca.markets' for live trading

# Define your scalping trading bot strategy
def scalping_strategy():
    # Get market data
    barset = api.get_barset('AAPL', '1Min', limit=2)  # Get the last two 1-minute bars for AAPL
    aapl_bars = barset['AAPL']
    
    # Check if there are enough bars for analysis
    if len(aapl_bars) < 2:
        return
    
    # Extract relevant data
    current_close = aapl_bars[-1].c
    previous_close = aapl_bars[-2].c
    
    # Implement your scalping trading logic
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

# Run the scalping trading bot
scalping_strategy()
