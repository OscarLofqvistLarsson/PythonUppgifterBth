import re


def sum_all(n):
    if n > 0:
        if n == 1:
            return 1
        return n + sum_all(n - 1)

print(sum_all(10))