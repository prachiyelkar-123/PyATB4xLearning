Fruit = input("Enter the fruit name, Mango, Dragoan, apple, banana\n")
Fruit = Fruit.lower()
match Fruit:
    case "Mango" | "Dragoan":
        print("love it")
    case "apple" | "banana":
        print("not loving this")
