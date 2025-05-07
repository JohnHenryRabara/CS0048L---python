
mylist = []

def mainprog():
    while True:
        print("To-Do list")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            addtask = input("What task to add: ").strip()
            addt(addtask)
        elif choice == 2:
            removetask = input("What task to remove: ")
            removet(removetask)
        elif choice == 3:
            print("Your Current Task: ")
            viewt()
        elif choice == 4:
            print("Exiting...")
            break

def addt(x):
    global mylist

    mylist.append(x)
    print("Task added!!!")
    print("")

def removet(x):
    global mylist

    if x in mylist:
        mylist.remove(x)
    print("Task removed!!!")
    print("")

def viewt():
    global mylist

    for list in mylist:
        print(f"Task: {list}")
    print("")



        

mainprog()
