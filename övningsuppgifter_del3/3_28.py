def numbers_between(start,end):
    if start == end:
        return str(start)
    return str(start) + "," + numbers_between(start +1,end)

print(numbers_between(2,7))