__author__ = "Beau Williams"
def main():
    total_items = int(input("Enter number of items: "))
    total_price = 0
    for i in range(0, total_items):
        item_price = int(input("Enter item " + str(i+1) + " price: "))
        total_price += item_price
    if total_price >= 100:
        print("You have qualified for a 10% discount!")
        total_price = total_price - (total_price / 100 * 10)
    print("The shipping total is: $" + str(total_price))
main()

