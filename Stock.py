stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 300,
    "GOOGL": 140,
    "AMZN": 130,
    "NVDA": 1100,
    "META": 480,
    "NFLX": 600
}

portfolio = []

while True:
    stock_name = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("Error: Stock not found. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        portfolio.append({"symbol": stock_name, "quantity": quantity})
    except ValueError:
        print("Invalid quantity. Please enter a number.")

# Calculate total
total_value = 0
for stock in portfolio:
    symbol = stock["symbol"]
    quantity = stock["quantity"]
    total_value += quantity * stock_prices[symbol]

print(f"\nTotal Investment Value: ${total_value:.2f}")

# Save to file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("=" * 25 + "\n")
    for stock in portfolio:
        symbol = stock["symbol"]
        quantity = stock["quantity"]
        price = stock_prices[symbol]
        file.write(f"{symbol}: {quantity} shares @ ${price} = ${quantity * price}\n")
    file.write("=" * 25 + "\n")
    file.write(f"TOTAL VALUE: ${total_value:.2f}")
