"""Assignment 2"""
def payingDebtOffInAYear(balance1, annualInterestRate):
    """Debt"""
    fixedpayment=0
    balance = balance1
    while balance > 0:
        balance = balance1
        month=1
        monthlyinterestrate=annualInterestRate/12.0
        fixedpayment = fixedpayment + 10
        while month<=12:
            monthlyunpaidbalance=balance-fixedpayment
            Updatedbalance=monthlyunpaidbalance+(monthlyinterestrate*monthlyunpaidbalance)
            balance=Updatedbalance
            month += 1
    return fixedpayment

def main():
    """Debt"""
    data = input()
    data = data.split(' ')
    data = list(map(float,data))
    print("Lowest payment:"+str(payingDebtOffInAYear(data[0],data[1])))
    
if __name__ == "__main__":
    main()