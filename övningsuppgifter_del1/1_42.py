import math
def estimate_pi(k):
    total = 0
    while k > 10 ** (-15):
        for i in range(k):
            const = math.factorial(4*i) * (1103 + 26390* i) / ((math.factorial(i) ** 4) * 396 ** (4*i))
            total += const
            k -= 1
    return 1 / ((2* math.sqrt(2))/(9801) * total)

print(estimate_pi(1000))
print(math.pi)