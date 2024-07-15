def calc_bank_investment(initial_money, number_of_years, rate):
    return initial_money * (( 1 + rate ) ** number_of_years)


print(calc_bank_investment(1000, 3, 0.2))

#=============================================================================

def calc_bank_investment(initial_money, number_of_years, rate):
    result = initial_money

    for i in range(number_of_years):
        result = result * ( 1 + rate)           # ~ result *= (1 + rate)

    return result

print(calc_bank_investment(1000, 3, 0.2))


#=============================================================================

def calc_bank_investment(initial_money, number_of_years, rate):
    result = initial_money

    for i in range(number_of_years):
        result = result * ( 1 + rate)           # ~ result *= (1 + rate)

    return result

print(calc_bank_investment(number_of_years=3, rate=0.2, initial_money=1000, ))