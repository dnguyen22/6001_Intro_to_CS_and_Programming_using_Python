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


balance = 80
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def find_min_fixed_monthly_payment(balance, annualInterestRate):
    """
    Calculates monthlyPayment
    :param balance:
    :param annualInterestRate:
    :return:
    """


def get_year_balance(balance, annualInterestRate, monthlyPaymentRate):
    """
    Calculates balance at the end of one year (12 months)
    :param balance: the outstanding balance on the credit card
    :param annualInterestRate: annual interest rate as a decimal
    :param monthlyPaymentRate: minimum monthly payment rate as a decimal
    :return: End of year balance
    """

    start_balance = balance

    for month in range(1, 13):
        end_balance = get_balance(start_balance, annualInterestRate, monthlyPaymentRate)
        #print("Month {} Remaining balance: {}".format(month, end_balance))
        start_balance = end_balance

    return end_balance


end_bal = get_year_balance(balance, annualInterestRate, monthlyPaymentRate)
print("Remaining balance: " + str(end_bal))