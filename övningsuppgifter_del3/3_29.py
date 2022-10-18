def two_pow_starts(n):
    if n == 0:
        return "*"
    return 2 * two_pow_starts(n - 1)
print(two_pow_starts(3))