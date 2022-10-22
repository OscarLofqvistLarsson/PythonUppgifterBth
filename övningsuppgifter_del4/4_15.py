from math import factorial
def pascal(n):
    return[[factorial(n) // (factorial(x) * factorial(n - x)) for x in range(n +1)] for n in range(n)]

print(pascal(10))


