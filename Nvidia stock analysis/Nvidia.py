import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the stock data (adjust for the format)
# Replace the file path with your actual path
data = pd.read_csv(r"C:\Users\Nvidia stock analysis\NVIDIA_STOCK.csv", skiprows=2)

# Set proper column names
data.columns = ['Date', 'Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']

# Step 2: Explore the data
print("Data Info:\n", data.info())
print("\nData Preview:\n", data.head())

# Step 3: Clean the data (optional, depending on your dataset)
# Check for missing values
if data.isnull().sum().sum() > 0:
    print("\nMissing values found. Filling with forward fill.")
    data.fillna(method='ffill', inplace=True)

# Convert 'Date' column to datetime format if not already
if not np.issubdtype(data['Date'].dtype, np.datetime64):
    data['Date'] = pd.to_datetime(data['Date'])

# Set 'Date' as index
data.set_index('Date', inplace=True)

# Step 4: Perform Analysis
# Calculate a 20-day moving average
data['20-Day MA'] = data['Close'].rolling(window=20).mean()

# Calculate daily returns
data['Daily Return'] = data['Close'].pct_change()

# Calculate volatility (standard deviation of daily returns)
data['Volatility (20 Days)'] = data['Daily Return'].rolling(window=20).std()

# Step 5: Visualization
plt.figure(figsize=(14, 7))

# Plot closing prices and moving averages
plt.subplot(2, 1, 1)
plt.plot(data.index, data['Close'], label='Closing Price', color='blue')
plt.plot(data.index, data['20-Day MA'], label='20-Day MA', color='orange', linestyle='--')
plt.title('NVIDIA Stock Price and Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Plot daily returns
plt.subplot(2, 1, 2)
plt.plot(data.index, data['Daily Return'], label='Daily Returns', color='green')
plt.axhline(0, color='red', linewidth=0.8, linestyle='--')
plt.title('Daily Returns of NVIDIA Stock')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.legend()

plt.tight_layout()
plt.show()

# Additional Insights
# Print key statistics
print("\nKey Statistics:")
print(f"Average Daily Return: {data['Daily Return'].mean():.4f}")
print(f"Volatility (Last 20 Days): {data['Volatility (20 Days)'].iloc[-1]:.4f}")
