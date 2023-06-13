import alpaca_trade_api as tradeapi
import requests

# Initialize the Alpaca API
api = tradeapi.REST('CKMGDFPR3405MOQJ2OP9', 'CDRbraR9PhRUlWAwEirrwWg0DAXgV64aVcuZuwJO', base_url='https://paper-api.alpaca.markets')  # Use 'https://api.alpaca.markets' for live trading

#connecting to airtable

url =  "https://api.airtable.com/v0/appSomN0g3WSQmzgZ/Projects"
auth_token = "pat2ey1ZIUiNVm3Pi.5a0e609cb6b06adeb95e91902448ad27645fa5f838892a1573cab26cc5ea99cd"

headers= {
    "authorization": f"Bearer {auth_token}"
    
}

response = requests.get(url,headers=headers)
data = response.json()

data

#check specific column in data frame

url =  "https://api.airtable.com/v0/appSomN0g3WSQmzgZ/Projects/recmavtv0NAwjIyMV"
auth_token = "pat2ey1ZIUiNVm3Pi.5a0e609cb6b06adeb95e91902448ad27645fa5f838892a1573cab26cc5ea99cd"

headers= {
    "authorization": f"Bearer {auth_token}"
    
}

response = requests.get(url,headers=headers)
data = response.json()

data

#input option to retrieve data

                                        
stock_ticker= input("what stock do you wish to trade? ")
    

print(stock_ticker)

# will not work on off market hours fromherer **** to ****
# Define your trading bot strategy
def trading_strategy():
    # Get market data
    barset = api.get_barset(stock_ticker, 'day', limit=2)  # Get the last two days of stock_ticker data
    aapl_bars = barset[stock_ticker]
    

 #Calculate support and resistance levels
    support_level = input( "example support price ") # Example support level
    resistance_level = input("example resistance price level ")  # Example resistance level


# Extract relevant data
    current_close = aapl_bars[-1].c
    previous_close = aapl_bars[-2].c


# check account balance
account = api.get_account()
cash_balance = float(account.cash)
print(f"Cash Balance: ${cash_balance:.2f}")
    


#  Implement trading logic with support and resistance levels
if current_close > resistance_level:
    # Price above resistance, potential breakout, place buy order
        if old_balance >= current_close:
            api.submit_order(symbol= stock_ticker, qty=1, side='buy', type='market', time_in_force='gtc')
        else:
            print("Insufficient funds for buy order.")
elif current_close < support_level:
        # Price below support, potential breakdown, place sell order
        api.submit_order(symbol=stock_ticker, qty=1, side='sell', type='market', time_in_force='gtc')
else:
        # Price within support and resistance range, the bot wil not trade
        pass

# Run the trading bot
trading_strategy()

# Get the updated cash balance *****here code temperorry error stops
account = api.get_account()
new_balance = float(account.cash)
print(f"New Balance: ${new_balance:.2f}")

#balance update.   ***code error stops here

def check_balance(old_balance, new_balance):
    if new_balance < old_balance:
        return -1
    elif new_balance > old_balance:
        return 1
    else:
        return 0


#udate balance

new_balance = input("balance?")

int(new_balance)

if int(new_balance) > 0:
    win_loss = "win"
    
else:
    win_loss = "loss"

print(win_loss)

## udate database with win loss outcome
url = "https://api.airtable.com/v0/appSomN0g3WSQmzgZ/Projects/reckgA4kow1Qw3hSp"
auth_token = "pat2ey1ZIUiNVm3Pi.5a0e609cb6b06adeb95e91902448ad27645fa5f838892a1573cab26cc5ea99cd"

headers = {
    "authorization": f"Bearer {auth_token}",
    "content-Type": "application/json"
}

 

payload = {
    "fields": {
        win_loss :3700+ 1,
        'total_trades' : 10000 +1
    }
}

response = requests.patch(url, headers=headers, json=payload)
response.json()