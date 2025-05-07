def celtofah(x):
    Fahrenheit = (x * 1.8) + 32
    print(f"Converted temperature = {Fahrenheit:.2f}")
    print("")

def fahtocel(x):
    celsius = (x - 32) / 1.8
    print(f"Converted temperature = {celsius:.2f}")
    print("")

def mainprog():
    while True:
        print("Temperature converter!!!")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = float(input("Enter temperature in Celsius: "))
            celtofah(value)
        elif choice == 2:
            value = float(input("Enter temperature in Fahrenheit: "))
            fahtocel(value)
        elif choice == 3:
            print("Exiting...")
            break

mainprog()
