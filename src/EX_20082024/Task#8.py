"""✅ Triangle Classifier:

Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal),

isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle."""

length_of_side1 = int(input("enter the length of side 1:"))
length_of_side2 = int(input("enter the length of side 2:"))
length_of_side3 = int(input("enter the length of side 3:"))

if length_of_side1 == length_of_side2 and length_of_side2 == length_of_side3:
    print("Triangle is equilateral")
elif length_of_side1 == length_of_side2:
    print("Triangle is isosceles 1")
elif length_of_side1!=length_of_side2 and length_of_side2==length_of_side3:
    print("Triangle is isosceles")
else:
    print("Triangle is scaiene")
