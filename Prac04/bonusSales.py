__author__ = "Beau Williams"
def main():
    sales = float(input("Enter sales: "))
    while sales < 0:
        sales = float(input("Enter sales: "))
        if sales <= 1000:
            ten_percent_calc(sales)
            updated_tenpercent_bonus = ten_percent_calc(sales)
            print("Bonus is: $ {:.2f}".format(updated_tenpercent_bonus))
        else:
            fifteen_percent_calc(sales)
            updated_fifteenpercent_bonus = fifteen_percent_calc(sales)
            print("Bonus is: $ {:.2f}".format(updated_fifteenpercent_bonus))
def ten_percent_calc(sales):
    ten_percent_bonus = sales - (sales / 100 * 10)
    return ten_percent_bonus
def fifteen_percent_calc(sales):
    fifteen_percent_bonus = sales - (sales / 100 * 15)
    return fifteen_percent_bonus
main()
