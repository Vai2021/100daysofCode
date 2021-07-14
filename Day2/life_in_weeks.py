age = input("What is your current age?")

remaining__age=90-int(age)
r_days = remaining__age* 365
r_weeks = remaining__age * 52
r_months = remaining__age * 12

print(f"You have {r_days} days, {r_weeks} weeks, and {r_months} months left.")