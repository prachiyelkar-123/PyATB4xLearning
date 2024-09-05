# Conditions and Loops

# Write a program to take a user age and let him know if he can go the club.
# 25

# Logic Building
# 1. user input - data type -> int
# o/p -> String -> user if he can go or not.


# 2. Rough loigc
# age  > 25 -> print can go
# age < 25 -> print can't go

#Logic

age = int(input("Enter the age"))

if age >= 25:
    print("He can go to club")
else:
    print("He Can't")
