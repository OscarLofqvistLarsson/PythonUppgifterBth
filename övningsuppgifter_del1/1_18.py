num = int(input("input a number"))

if num % 2 == 0:
    print("the number is even")

    if num & 3 == 0:
        print("and is multipel of 4")
    else:
        pass

elif num % 2 == 1:
    print("the number is odd")

else:
    print("something went wrong try again")


number = int(input("number to divide"))
divisor = int(input("number to divide with"))



if number % divisor == 0:
    print("divided equal")
else:
    print("not divided equal")