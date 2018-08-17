"""Assignment - 3"""
def paying_debt(balance, annual_interest_rate):
    """Bisection Meth"""
    monthly_interest_rate = (annual_interest_rate) / 12.0
    month_payment_low_bound = balance / 12.0
    month_payment_up_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0
    new_balance = balance
    epsilon_ = 0.0001
    guess_ = (month_payment_low_bound + month_payment_up_bound)/2.0
    while True:
        month_ = 1
        while month_ <= 12:
            new_balance = new_balance - guess_
            new_balance = new_balance + (monthly_interest_rate * new_balance)
            month_ += 1
        if new_balance > 0 and new_balance > epsilon_:
            month_payment_low_bound = guess_
            new_balance = balance
        elif new_balance < 0 and new_balance < -epsilon_:
            month_payment_up_bound = guess_
            new_balance = balance
        else:
            return round(guess_, 2)
        guess_ = (month_payment_low_bound + month_payment_up_bound)/2

def main():
    """Bisection Meth"""
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: ",str(paying_debt(data[0], data[1])))
if __name__ == "__main__":
    main()
