import math
def leibniz(number):
    total = 0
    for i in range(number):
        const = (-1) ** i /(2 * i + 1)
        total += const
    return total * 4

print(leibniz(1))
print(math.pi)