def same_content(tup1, tup2):
    for x in tup1:
        for y in tup2:
            if x in tup1 and y in tup1 and len(tup1) == len(tup2) and tup1.count(x) == tup2.count(y):
                return True
            else:
                return False


print(same_content((1, 2), (1,2)))