try:
    a = int(input("Input number to divide"))
    b = int(input("Input number as divider"))
    print(a / b)
except ValueError as error:
    print("Error", error)
except ZeroDivisionError as error:
    print("Error", error)