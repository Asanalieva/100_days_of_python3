# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name and surname? \n").lower()
name2 = input("What is her/his name and surname? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1 + name2
t=names.count("t")
r=names.count("r")
u=names.count("u")
e=names.count("e")
true = t+r+u+e

l=names.count("l")
o=names.count("o")
v=names.count("v")
e=names.count("e")
love = l+o+v+e

print("T occures",t,"times")
print("R occures",r,"times")
print("U occures",u,"times")
print("E occures",e,"times")

print("Total=",true)

print("L occures",l,"times")
print("O occures",o,"times")
print("V occures",v,"times")
print("E occures",e,"times")
print("Total=",love)

love_score = str(love)+str(true)
emoji = "\U0001F49A \U00002764 "
print(f"Your love percenage is: {love_score}",emoji)
