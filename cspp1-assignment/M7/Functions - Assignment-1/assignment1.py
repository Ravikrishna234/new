"""Monthly balance"""
def paying_debtoff(balance, annual_interest_rate, monthly_payment_rate):
    """balance"""
    monthly_interest_rate = annual_interest_rate/12.0
    updated_balance = balance
    month_ = 1
    while month_ <= 12:
        minimum_monthly_payment = monthly_payment_rate * updated_balance
        monthly_unpaid_balance = updated_balance - minimum_monthly_payment
        updated_balance = monthly_unpaid_balance + (monthly_unpaid_balance*monthly_interest_rate)
        p_in = round(updated_balance, 2)
        month_ += 1
    print("Remaining balance:", p_in)
def main():
    """balance"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    paying_debtoff(data[0], data[1], data[2])

if __name__ == "__main__":
    main()
