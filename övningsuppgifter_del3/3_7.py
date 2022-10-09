def not_common(tup1, tup2):
    res_list = []
    for x in tup1:
        if x not in tup2:
            res_list.append(x)
    for x in tup2:
        if x not in tup1:
            res_list.append(x)
    res_list.sort()
    return tuple(res_list)
print(not_common((1, 2, 3, 4), (3, 4, 5, 6)))