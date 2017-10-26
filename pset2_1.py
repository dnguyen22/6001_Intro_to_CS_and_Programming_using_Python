# Paying Debt off in a Year

def get_balance(balance, annualInterestRate, monthlyPaymentRate):
    """
    :param balance: the outstanding balance on the credit card
    :param annualInterestRate: annual interest rate as a decimal
    :param monthlyPaymentRate: minimum monthly payment rate as a decimal
    :return: credit card balance after one month
    """
    monthlyInterestRate = annualInterestRate / 12.0
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    updatedBalance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance

    return round(updatedBalance, 2)

init_balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

start_balance = init_balance

for month in range(1,13):
    end_balance = get_balance(start_balance, annualInterestRate, monthlyPaymentRate)
    print("Month {} Remaining balance: {}".format(month, end_balance))
    start_balance = end_balance

print("Remaining balance: " + str(end_balance))

