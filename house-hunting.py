portion_down_payment = 0.25
current_savings = 0
r = 0.04

annual_salary_as_str = input("Enter your annual salary: ")
annual_salary = int(annual_salary_as_str)
portion_saved_as_str = input("Enter the percent of your salary to save, as a decimal: ")
portion_saved = float(portion_saved_as_str)
cost_of_home_as_str = input("Enter the cost of your dream home: ")
cost_of_home = int(cost_of_home_as_str)

if annual_salary > 0:
    (annual_salary * portion_down_payment) == current_savings
    (current_savings + (current_savings * r/12)) == num_months
else: 
    print("You have no money to save! Sorry.")

print("Number of months: ", num_months)