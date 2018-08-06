"""Assignment - 3"""
def paying_debt(balance_1, annual_interest_rate):
    """Bisection Meth"""
    monthly_interest_rate = (annual_interest_rate) / 12.0
    month_payment_low_bound = balance_1 / 12
    month_payment_up_bound = (balance_1 * (1 + monthly_interest_rate)**12) / 12.0
    new_balance = balance_1
    eps_ilon = 0.0001
    gu_ess = (month_payment_low_bound + month_payment_up_bound)/2.0
    while True:
        month_ = 1
        while month_ <= 12:
            new_balance = new_balance - gu_ess
            new_balance = new_balance + (monthly_interest_rate * new_balance)
            month_ += 1
        if new_balance > 0 and new_balance > eps_ilon:
            month_payment_low_bound = gu_ess
            new_balance = balance_1
        elif new_balance < 0 and new_balance < -eps_ilon:
            month_payment_up_bound = gu_ess
            new_balance = balance_1
        else:
            return (gu_ess, 2)

        gu_ess = (month_payment_low_bound + month_payment_up_bound)/2

def main():
    """Bisection Meth"""
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: "paying_debt(data[0], data[1]))
if __name__ == "__main__":
    main()
