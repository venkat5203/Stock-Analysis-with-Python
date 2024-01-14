import yfinance as yf
import matplotlib.pyplot as plt
stock_symbol = "AAPL"
start_date = "2022-01-01"
end_date = "2023-12-20"
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
print(stock_data.head())
stock_data['Daily_Return'] = stock_data['Close'].pct_change()
stock_data['EMA_20'] = stock_data['Close'].rolling(window=50).mean()
stock_data['Volatility'] = stock_data['Daily_Return'].std()
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['EMA_20'], label='20-day EMA', linestyle='--')
plt.title(f'Stock Price Analysis for {stock_symbol}')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
plt.figure(figsize=(8, 5))
plt.hist(stock_data['Daily_Return'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title('Daily Returns Distribution')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.show()
