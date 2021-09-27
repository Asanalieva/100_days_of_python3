for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

''' program will print each number from 1 to 100 in turn.` 

>   `When the number is divisible by 3 then instead of printing the number it will print "Fizz".` 

>     `When the number is divisible by 5, then instead of printing the number it will print "Buzz".` 

>       `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it will print "FizzBuzz" '''
