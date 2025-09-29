# Ask the user for monthly income

monthly_income = float(input("Enter your monthly income: "))

# Ask the user for monthly expenses

monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings (income - expenses)

monthly_savings = monthly_income - monthly_expenses

# Project annual savings (12 months of savings + 5% interest)

annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Printing the results
print(f"Your monthly savings are: ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")