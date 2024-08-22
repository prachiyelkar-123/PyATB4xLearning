"""✅ FizzBuzz Test:

Write a program that prints numbers from 1 to 100. # Loop For

However, for multiples of 3, print "Fizz" instead of the number, and

for multiples of 5, print "Buzz."

For numbers that are multiples of both 3 and 5, print "FizzBuzz."
"""


num = int(input("Enter number: \n"))

for num in range(1, 100):
    if num%3 == 0:
        print("Fizz")
    elif num%5 ==0:
        print("Buzz")
    else:
        print("FizzBuzz")