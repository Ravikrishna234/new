"""Assignment 2"""
def paying_debtoff(mainbalance_1, annual_interest_rate):
    """Debt"""
    fixed_payment = 0
    temp_balance = mainbalance_1
    while temp_balance > 0:
        temp_balance = mainbalance_1
        month_ = 1
        monthly_interest_rate = annual_interest_rate / 12.0
        fixed_payment = fixed_payment + 10
        while month_ <= 12:
            monthly_unpaid_balance = temp_balance - fixed_payment
            updated_balance = monthly_unpaid_balance+(monthly_interest_rate*monthly_unpaid_balance)
            temp_balance = updated_balance
            month_ += 1
    return fixed_payment

def main():
    """Debt"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest payment: "+str(paying_debtoff(data[0], data[1])))
if __name__ == "__main__":
    main()
