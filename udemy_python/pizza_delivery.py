print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
  bill+=15
elif size == "M":
  bill = bill + 20

elif size == "L":
  bill += 25


if size == "S" and add_pepperoni == "Y":
  bill += 2
if size == "M" or "L" and  add_pepperoni == "Y":
  bill += 3

if extra_cheese == "Y":
  bill+=1
print(f"Your final bill is: ${bill}")


'''
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
'''