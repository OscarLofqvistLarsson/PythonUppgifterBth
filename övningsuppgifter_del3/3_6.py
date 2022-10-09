def common_content(tup1, tup2):
    res = ()
    for x in tup1:
            if x in tup2:
                res += (x,)
    return res

print(common_content((1, 2, 3, 'p', 'n'), (2, 5 , 1, 'p')))