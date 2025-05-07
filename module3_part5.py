mylistsub = []
mylistgrade = []

def mainprog():
    
    while True:
        print("Student Grade Calculator")
        print("1. Add Score")
        print("2. Calculate Average")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
    
        if choice == 1:
            toaddsub = input("Enter subject: ")
            toaddgrade = float(input("Enter grade for that subject: "))
            addscore(toaddsub, toaddgrade)
            print("")
        elif choice == 2:
            calcuave()
            print("")
        elif choice == 3:
            print("exiting...")
            break
        else:
            print("invalid choice...")


def addscore(x,y):
    global mylistsub
    global mylistgrade

    mylistsub.append(x)
    mylistgrade.append(y)
    
def calcuave():
    global mylistgrade
    
    foraverageadd = 0
    
    for list in mylistgrade:
        foraverageadd += list
    
    result = foraverageadd / len(mylistgrade)
    print(f"Average = {result}")

mainprog()
