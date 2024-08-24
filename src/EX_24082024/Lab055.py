def print_arguments(*args):
    # *args = multiple argument with no limit, -> list
    #print(args[0])
  for i in args:
        print(i)

# list = ["pramod", "amit", "lucky"]

print_arguments("prachi", "pradnya", "prajakta")
print_arguments("alka", "eknath")
print_arguments("alka", 10)
print_arguments("pooja", 10, True)
print_arguments("priya", 10, True, False)
print_arguments("amit", 10, True, False, "Prachi")
print_arguments("lucky")
# print_arguments() -minimum 1 arguement is importa


print("pradnya")
print("prachi", "alka")
print("alka", "pradnya", True)
print("prajakta", "pooja", True, False)