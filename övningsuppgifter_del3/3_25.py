def count_X(string):
    if len(string) < 1:
        return 0
    else:
        c = 0
        if string[0] == "X":
            c = 1
        return c + count_X(string[1:])

print(count_X("axe"))