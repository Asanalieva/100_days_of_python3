total = int(input("What was the total bill? "))
people = int(input("How many people split the bill? "))
tip = int(input("How much tip would you like to give? 10%,12% or 15%  "))

tip_as_percent = tip / 100
total_tip_amount = total * tip_as_percent
total_bill = total + total_tip_amount
bill_per_person = total_bill / people
final_amont = round(bill_per_person, 2)
#Result
print(f"Each person should pay: ${final_amont}")