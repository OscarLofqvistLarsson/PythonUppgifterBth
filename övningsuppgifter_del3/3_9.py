def sort_by_len(tup_list, direction):
    lst= []
    for x in tup_list:
        lst.append((len(x), x))
    lst.sort()
    if direction == 'des':
        lst = lst[::-1]
    res = ()
    for x in lst:
        res += (x[1],)
    return res

print(sort_by_len(('Windows', 'Linux', 'OSX'), 'des'))