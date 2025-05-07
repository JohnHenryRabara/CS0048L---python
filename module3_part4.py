toguess = 0

def mainprog():
        print("Guessing Game!!!")
        print("1. Play Number Guessing Game")
        print("2. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            while True:
                fromuser = int(input("Guess a number from 1 - 100: "))
                if fromuser == toguess:
                    print("Right guess!!!")
                    break
            else:
                print("try again!!!")
        elif choice == 2:
            print("exiting...")


def random():
    import random
    global toguess

    a = random.randint(1,100)
    toguess += a
    print(toguess)

# random() //to show the right value
mainprog()