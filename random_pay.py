# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

person = random.choice(names)
print(person, "is going to buy the meal today!")





