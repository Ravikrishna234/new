"""Assignment - 3"""
def payingDebtOffInAYear(balance, annual_interest_rate):
    """Bisection Meth"""
    monthly_interest_rate = (annual_interest_rate) / 12.0
    monthly_payment_lower_bound = balance / 12
    monthly_payment_upper_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0
    new_balance = balance
    epsilon = 0.0001
    guess = (monthly_payment_lower_bound + monthly_payment_upper_bound)/2.0
    while True:
        month = 1
        while month <= 12:
            new_balance = new_balance - guess
            new_balance = new_balance + (monthly_interest_rate * new_balance)
            month += 1
        if new_balance > 0 and new_balance > epsilon:
            monthly_payment_lower_bound = guess
            new_balance = balance
        elif new_balance < 0 and new_balance < -epsilon:
            monthly_payment_upper_bound = guess
            new_balance = balance
        else:
            return guess

        guess = (monthly_payment_lower_bound + monthly_payment_upper_bound)/2

def main():
    """Bisection Meth"""
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print(payingDebtOffInAYear(data[0],data[1]))
    
if __name__== "__main__":
    main()
