import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
price = INITIAL_PRICE
print("Starting price: $" + str(INITIAL_PRICE))
day = 0
while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    day += 1
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + price_change)
    print("On day " + str(day) + " price: ${:,.2f}".format(price))

