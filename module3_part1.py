def add(x, y):
    print("Adding...")
    return x + y
    print("")

def subtract(x,y):
    print("subtracting...")
    return x - y
    print("")

def multiply(x,y):
    print("multiplying...")
    return x * y
    print("")

def divide(x,y):
    print("dividing...")
    return x / y
    print("")

def mainfunc():
    while True:
        print("Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            firstno = int(input("Enter first number:"))
            secondno = int(input("Enter second number:"))
            result = add(firstno,secondno)
            print(f"Result = {result:.2f}")
        elif choice == 2:
            firstno = int(input("Enter first number:"))
            secondno = int(input("Enter second number: "))
            result = subtract(firstno,secondno)
            print(f"Result = {result:.2f}")
        elif choice == 3:
            firstno = int(input("Enter first number:"))
            secondno = int(input("Enter second number: "))
            result = multiply(firstno,secondno)
            print(f"Result = {result:.2f}")
        elif choice == 4:
            firstno = int(input("Enter first number:"))
            secondno = int(input("Enter second number: "))
            result = divide(firstno, secondno)
            print(f"Result = {result:.2f}")
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid Choice!")

mainfunc()
