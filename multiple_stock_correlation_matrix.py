import yfinance as yf
import pandas as pd

# Define the stock symbols
stock_symbols = ['CCOLA.IS', 'XU030.IS', 'SISE.IS', 'THYAO.IS', 'XU100.IS']


# Define the start and end dates for historical data
start_date = '2022-01-01'
end_date = '2023-01-01'

# Download historical data from Yahoo Finance
stock_data = yf.download(stock_symbols, start=start_date, end=end_date)['Adj Close']

# Calculate the correlation matrix
correlation_matrix = stock_data.corr()

print(correlation_matrix)

