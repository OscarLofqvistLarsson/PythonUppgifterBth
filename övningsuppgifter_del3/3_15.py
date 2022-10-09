def reverse_lookup(dict, value):
    lst = []
    for k in dict:
        if dict[k] == value:
            lst.append(k)
        lst.sort()
    return lst


print(reverse_lookup({'a':1, 'b':1, 'c':2}, 1))