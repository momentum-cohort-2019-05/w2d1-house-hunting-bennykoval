portion_down_payment = 0.25
returns = 0.04
current_savings = 0
months = 0

annual_salary_as_str = input("Enter your annual salary: ")
annual_salary = int(annual_salary_as_str)
portion_saved_as_str = input("Enter the percent of your salary to save, as a decimal: ")
portion_saved = float(portion_saved_as_str)
cost_of_home_as_str = input("Enter the cost of your dream home: ")
cost_of_home = int(cost_of_home_as_str)

down_cost = cost_of_home * portion_down_payment

if annual_salary > 0:
    monthly_savings = (annual_salary / 12) * portion_saved
else: 
    print("Sorry - you have no income to save!")

while current_savings < down_cost:
    months += 1
    current_savings += monthly_savings + (current_savings * (returns / 12))
    #print("Debug returns " + str(returns))
    #print("Debug current_savings ") + (str(current_savings))
    #print("Debug months ") + (int(months))
    #I AM SCREAMING!

print("Number of months: ", months)

