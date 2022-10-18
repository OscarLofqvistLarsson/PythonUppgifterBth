import re


def pascal(k,i):
    if i > k:
        return "invalid"
    elif k == 0 or i == 0 or k == i:
        return 1
    return pascal(k - 1, i - 1) + pascal(k - 1, i)

print(pascal(5,3))