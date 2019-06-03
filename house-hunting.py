portion_down_payment = 0.25
r = 0.04

annual_salary_as_str = input("Enter your annual salary: ")
annual_salary = int(annual_salary_as_str)
portion_saved_as_str = input("Enter the percent of your salary to save, as a decimal: ")
portion_saved = float(portion_saved_as_str)
cost_of_home_as_str = input("Enter the cost of your dream home: ")
cost_of_home = int(cost_of_home_as_str)

if annual_salary > 0
    current_savings = (annual_salary * portion_down_payment)
else: 
    print("Sorry - you have no income to save!")

print("Number of months: ", (current_savings + (current_savings * r/12)))