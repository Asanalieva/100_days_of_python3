# BMI = Body Mass Index

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
result = round(weight / (height ** 2))

if result < 18.5:
    print("Result is", result, 'you\'re underweight')
elif result < 25:
    print("Result is", result, 'you have normal weight')
elif  result < 30:
    print("Result is", result, 'you\'re overweight')
elif result < 35:
    print("Result is", result, 'you\'re obese')
else:
    print("Result is", result, 'you\'re clinically obese')