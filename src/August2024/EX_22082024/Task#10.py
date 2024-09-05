"""Task #10 -
✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24"""


num1 = int(input("Enter the number1"))
fact = 1
for i in range(1, num1+1):
    fact=fact*i
    print(f"Factorial of {num1} is {fact}")

# fact 1*1= 1
# fact 1*2 = 2
#fact 2*3  = 6
#fact 6*4 = 24
#fact 24*5 = 120
