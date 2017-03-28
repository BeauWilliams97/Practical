__author__ = "Beau Williams"
def main():
    TARIFF_11 = 0.244618
    TARIFF_31 = 0.136928
    cents_per_kwh = int(input("Which tariff? 11 or 31: "))
    while cents_per_kwh != 11 or cents_per_kwh != 31:
        print("Invalid input.")
        cents_per_kwh = int(input("Which tariff? 11 or 31: "))
    else:
        dailyuse_per_kwH = float(input("enter daily use per kWh: "))
        number_billing_days = int(input("enter number of billing days: "))
        estimated_bill = bill_calculation(dailyuse_per_kwH, cents_per_kwh, number_billing_days)
        print("Estimated bill: {}".format(estimated_bill))

def bill_calculation(, dailyuse_per_kwh, number_billing_days):
    return (cents_per_kwh * dailyuse_per_kwh) * number_billing_days

main()
