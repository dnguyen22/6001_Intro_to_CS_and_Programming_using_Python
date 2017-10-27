# Paying Debt off in a Year


def find_min_fixed_monthly_payment(balance, annual_interest_rate):
    """
    Calculates minimum monthly payment to pay off balance in 12 months
    :param balance: the outstanding balance on the credit card
    :param annual_interest_rate: annual interest rate as a decimal
    :return: lowest fixed payment needed to pay off balance in 12 months in steps of $10
    """
    def year_end_balance(balance, annual_interest_rate, fixed_monthly_payment):
        """
        Calculates balance at the end of one year (12 months)
        :param balance: the outstanding balance on the credit card
        :param annual_interest_rate: annual interest rate as a decimal
        :param fixed_monthly_payment: fixed monthly payment in multiples of $10
        :return: lowest fixed payment needed to pay off balance in 12 months in steps of $10
        """
        current_balance = balance
        monthly_interest_rate = annual_interest_rate / 12.0

        for month in range(1, 13):
            monthly_unpaid_balance = current_balance - fixed_monthly_payment
            current_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance

        return current_balance

    fixed_monthly_payment = 10

    while True:
        if year_end_balance(balance, annual_interest_rate, fixed_monthly_payment) > 0:
            # Fixed monthly payment increased by $10 to make balance 0 after 1 year
            fixed_monthly_payment += 10
        else:
            return fixed_monthly_payment


balance = 4773
annualInterestRate = 0.2

lowest_pay = find_min_fixed_monthly_payment(balance, annualInterestRate)
print("Lowest Payment: " + str(lowest_pay))