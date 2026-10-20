import csv

print("STOCK PORTFOLIO TRACKER")

symbol = input("Enter Stock Symbol: ").upper()
buy_price = float(input("Enter Buy Price: "))
shares = int(input("Enter Shares: "))

# Sample Current Prices
if symbol == "AAPL":
    current_price = 220

elif symbol == "MSFT":
    current_price = 520

elif symbol == "AMZN":
    current_price = 260

else:
    print("Invalid Symbol")
    exit()

investment = buy_price * shares
current_value = current_price * shares

profit = current_value - investment

print("\nPortfolio Summary")
print("Symbol:", symbol)
print("Investment:", investment)
print("Current Value:", current_value)
print("Profit/Loss:", profit)

with open("portfolio_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Symbol",
        "Investment",
        "Current Value",
        "Profit/Loss"
    ])

    writer.writerow([
        symbol,
        investment,
        current_value,
        profit
    ])

print("\nData saved in portfolio_summary.csv")