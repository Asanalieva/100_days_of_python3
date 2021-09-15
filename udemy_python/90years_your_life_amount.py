#How many time left to live if you could to live up to 90years?
age = int(input("What is your current age?"))


year = 90 - age
convert_to_days = year * 365
convert_to_weeks = year * 52
month = year * 12
print("You have",convert_to_days,"days",convert_to_weeks,"weeks",month,"month",year,"years","to live")
