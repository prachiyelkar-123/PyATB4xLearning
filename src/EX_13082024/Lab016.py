#String

name ="Prachi"
Middle_name = "Ekanth"
Last_Name = "Yelkar"
Full_Name = name+Middle_name+Last_Name

print(type(name))
print(Middle_name.upper())
print(Last_Name.lower())
print(len(name+Middle_name+Last_Name))

#Concatinate

print(name, Middle_name, Last_Name, sep=" ")
print(Full_Name)

#str

test= name+ "1"
print(test)

test1 = name + str(2)
print(test1)

# null is not present in Python
How_are_you = None
print(type(How_are_you))

How_are_you = "0"
print(type(How_are_you))

How_are_you = 0
print(type(How_are_you))

#id store memory
mark = 45
mark2 = 45
mark3 = 90
print(id(mark)) #140709110157112
print(id(mark2)) #140709110157112
print(id(mark3)) #140709110158552

