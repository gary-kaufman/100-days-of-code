print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? $"))
num_of_people = float(input("How many people want to split the bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100

# Tip calculation
amount_per_person = (total_bill / num_of_people) * (1 + tip_percentage)
rounded_amount_per_person = round(amount_per_person, 2)
rounded_amount_per_person = "{:.2f}".format(amount_per_person)
# Print payment amount for each person
print(f"Each person should pay: ${rounded_amount_per_person}")
