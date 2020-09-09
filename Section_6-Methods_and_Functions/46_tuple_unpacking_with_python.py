
# stock_prices = [('APP', 200),('GOOG',400),('MSFT',100)]

# for item in stock_prices:
#     print(item)

# for ticker,price in stock_prices:
#     print(ticker)

#     print(price+(0.1 * price))


work_hours = [('Abby',100),('Billy',400),('Cassie', 800)]

def employee_check(work_hours):
    current_max=0
    employee_of_month = ''

    for emp,hrs in work_hours:
        if hrs > current_max:
            current_max = hrs
            employee_of_month = emp
        else:
            pass

    return (employee_of_month, current_max)

print(employee_check(work_hours))

# Tuples unpacking with a function call
name,hours = employee_check(work_hours)
print(name)
print(hours)



