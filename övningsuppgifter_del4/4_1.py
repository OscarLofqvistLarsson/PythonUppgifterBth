def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

assert fibonacci(7) == 13
assert fibonacci(1) == 1


# divide by zero error
a = "1"
b = "0"
print(int(a) / int(b))

try:
    print(int(a) / int(b))
except ZeroDivisionError as error:
    print("Error message: ", error)


#value error
a = "#"
b = "0"
print(int(a) / int(b))

try:
    print(int(a) / int(b))
except ValueError as error:
    print("Error message" , error)

