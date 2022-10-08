
def menu():

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")
    choice = int(input("Your choice: "))
    return choice

def calculator():

    print("\n\nWelcome to Calculator")
    choice = -1
    number1 = 0
    number2 = 0
    while choice != 0:
        choice = menu()
        if choice == 0:
            pass
        elif choice < 0 or choice > 4:
            print("Input must be either 0,1,2,3,4.")
        else:
            if choice == 1:
                print("Choose your numbers")
                number1 = int(input("Number 1: "))
                number2 = int(input("Number 2: "))
                result = number1 + number2
            elif choice == 2:
                print("Choose your numbers")
                number1 = int(input("Number 1: "))
                number2 = int(input("Number 2: "))
                result = number1 - number2
            elif choice == 3:
                print("Choose your numbers")
                number1 = int(input("Number 1: "))
                number2 = int(input("Number 2: "))
                result = number1 * number2
            else:
                if number2 != 0:
                    result = number1 // number2
                else:
                    result = "Divide by zero is not possible!"
            print("Result: ", result, "\n")

if __name__ == "__main__":
    calculator()
