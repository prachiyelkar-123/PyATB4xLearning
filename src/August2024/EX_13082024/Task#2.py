"""Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}"""

num1 = float(input("enter the num1"))
num2 = int(input("enter the num2"))
print(f"max_number_between num1 and num2 is : {max(num1, num2)}")
print(f"power number_between num1 and num2 is : {pow(num1, num2)}")
print("Sum is", num1+num2)
print("Sub is", num1-num2)
print("Mul is", num1*num2)
print("Div is", num1/num2)
formated_number = f"{num1:.3f}"
print(formated_number)

