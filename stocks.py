stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]
print(len(stock_prices))

day_no = int(input("Enter day number: "))
def prince_at(x):
    print("Stock price = " + str(stock_prices[x - 1]))
prince_at(day_no)

first = int(input("Enter first day number: "))
last = int(input("Enter last day number: "))
edit_stock_prices = []

# create new list to hold the stock prices between the first and last day

def max_price():
    for i in range(first, last +1):
        edit_stock_prices.append(stock_prices[i])
    print(edit_stock_prices)
    print("Max price = " + str(max(edit_stock_prices)))
max_price()

def min_price():
    for i in range(first, last +1):
        edit_stock_prices.append(stock_prices[i])
    # print(edit_stock_prices)
    print("Minimum price = " + str(min(edit_stock_prices)))
min_price()