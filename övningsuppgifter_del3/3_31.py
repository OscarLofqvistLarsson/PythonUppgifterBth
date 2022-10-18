def two_factors(n):
    if n == 1:
        return "1"
    elif n % 2 == 0:
        return "2 * " + " ".join(two_factors(n // 2).split(" ")[::-1])
    return str(n)

print(two_factors(30))


