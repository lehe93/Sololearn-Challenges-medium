sum = 0

prices = input().split(",")

prices_of_items = []

for price in prices:
    prices_of_items.append(float(price))

for price in prices_of_items:
    sum += price

taxed_sales = sum * 1.07

discount_sales = (max(prices_of_items) + (sum - max(prices_of_items)) * 0.7) * 1.07

import math
total_saving = math.floor(taxed_sales - discount_sales)

print(total_saving)