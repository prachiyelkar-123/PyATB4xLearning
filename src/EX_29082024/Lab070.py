# List
# List - Collection of Items( Duplicate is allowed)

my_list = [1, 2, 3]  # Same type of data (int)
# my_list2 = [1, True, "Pramod", 12.34]

print(my_list)
print(len(my_list))

my_list[0] = "prachi"
my_list[1] = "Yelkar"
my_list[2] = "alka"

print("element at the index 0 - ", my_list[0])
print("element at the index 0 - ", my_list[1])
print("element at the index 0 - ", my_list[2])

print(my_list)

for element in my_list:
    print(element)


#append
my_list.append("eknath")
my_list.append(4)
print(my_list)

#add multiple

my_list.extend(["pradnya",5.30,6,7,True])
print(my_list)

#insert
my_list.insert(2    ,"pooja")
print(my_list)

print(len(my_list))

#replace
my_list[2] = "A"
print(my_list)

#remove
my_list.remove("A")
print(my_list)


