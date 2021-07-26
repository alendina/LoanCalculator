import argparse
import math

# -------------------------------
# read income parameters

parser = argparse.ArgumentParser(description="The calculator the capacity to compute differentiated payments")

parser.add_argument("--type", help="indicates the type of payment: 'annuity' or 'diff' (differentiated)")
parser.add_argument("--payment", type=float, help="is the monthly payment amount")
parser.add_argument("--principal", type=int, help="is used for calculations of both types of payment. You can get its value \
                                      if you know the interest, annuity payment, and number of months")
parser.add_argument("--periods", type=int, help="denotes the number of months needed to repay the loan. It's calculated based \
                                      on the interest, annuity payment, and principal")
parser.add_argument("--interest", type=float, help="is specified without a percent sign. Note that it can accept a \
                                      floating-point value")

args = parser.parse_args()
type_of_payment = args.type
annuity_payment = args.payment
loan_principal = args.principal
number_of_periods = args.periods
loan_interest = args.interest

# -------------------------------
# check income parameters

param_existence = [bool(loan_interest), bool(annuity_payment), bool(loan_principal),\
                   bool(number_of_periods), bool(loan_interest)]
# print(param_existence)

# -------------------------------
incorrect_parameters = False
calc_type = ''
if param_existence == [1, 0, 1, 1, 1]:
    if type_of_payment == "diff":
        # calculating differentiated payments (Exam 4) (Exam 1)
        calc_type = 'd'
    elif type_of_payment == "annuity":
        # calculate the annuity payment (Exam 2)
        calc_type = 'a'
    else:
        incorrect_parameters = True
elif param_existence == [1, 1, 1, 0, 1]:
    if type_of_payment == "annuity":
        # calculate how long it will take to repay a loan (Exam 6)
        calc_type = 'n'
    else:
        incorrect_parameters = True
elif param_existence == [1, 1, 0, 1, 1]:
    if type_of_payment == "annuity":
        # calculate the principal (Exam 5)
        calc_type = 'p'
    else:
        incorrect_parameters = True
else:
    incorrect_parameters = True

# check correction of parameter PAYMENT
if bool(annuity_payment):
    if annuity_payment <= 0:
        incorrect_parameters = True

# check correction of parameter PRINCIPAL
if bool(loan_principal):
    if loan_principal <= 0:
        incorrect_parameters = True

# check correction of parameter PERIOD
if bool(number_of_periods):
    if number_of_periods <= 0:
        incorrect_parameters = True

# check correction of parameter INTEREST
if bool(loan_interest):
    if loan_interest <= 0:
        incorrect_parameters = True
    else:
        loan_interest = loan_interest / (12 * 100)

# -------------------------------
if incorrect_parameters:
    print('Incorrect parameters')
    exit()

# ---------------------------------
# P - loan_principal
# A - annuity_payment
# i - loan_interest
# n - number_of_periods
# m - month
# ---------------------------------

if calc_type == 'd':
    # D1 = P/n + i*(P−P*(m−1)/n)
    calc_all_months = []
    for m in range(1, number_of_periods + 1):
        calc_for_month = loan_principal / number_of_periods \
            + loan_interest * (loan_principal - loan_principal * (m - 1) / number_of_periods)
        calc_for_month = math.ceil(calc_for_month)
        calc_all_months.append(calc_for_month)
        print(f'Month {m}: payment is {calc_for_month}')
    overpayment = sum(calc_all_months) - loan_principal
    print(overpayment)

elif calc_type == 'n':
    # n = log(A/(A-i*P), 1+i)
    n = math.log(annuity_payment / (annuity_payment - loan_interest * loan_principal), 1 + loan_interest)
    n = math.ceil(n)

    years = math.floor(n / 12)
    months = math.ceil(n - years * 12)
    # print(years, months)
    if years == 0 and months == 1:
        str_ = str(months) + ' month'
    elif years == 0 and months > 1:
        str_ = str(months) + ' months'
    elif years == 1 and months == 0:
        str_ = str(years) + ' year'
    elif years > 1 and months == 0:
        str_ = str(years) + ' years'
    elif years == 1 and months == 1:
        str_ = str(years) + ' year and ' + str(months) + ' month'
    elif years == 1 and months > 1:
        str_ = str(years) + ' year and ' + str(months) + ' months'
    else:
        str_ = str(years) + ' years and ' + str(months) + ' months'
    # print(str_)
    print(f'It will take {str_} to repay this loan!')
    overpayment = annuity_payment * n - loan_principal
    print(overpayment)

elif calc_type == 'a':
    # a = P * (i*pow(1+i,n)/(pow(1+i,n)-1))
    a = loan_principal * loan_interest * math.pow(1 + loan_interest, number_of_periods) \
        / (math.pow(1 + loan_interest, number_of_periods) - 1)
    print(f'Your monthly payment = {math.ceil(a)}!')
    overpayment = math.ceil(a) * number_of_periods - loan_principal
    print(round(overpayment))

elif calc_type == 'p':
    # p = A/(i*pow((1+i,n)/(pow(1+i,n)-1))
    p = annuity_payment / (loan_interest * math.pow(1 + loan_interest, number_of_periods) / (math.pow(1 + loan_interest, number_of_periods) - 1))
    print(f'Your loan principal = {math.floor(p)}!')
    overpayment = annuity_payment * number_of_periods - math.floor(p)
    print(round(overpayment))