def sort_by_number(tup_list):
    tup_list.sort()
    tup = ()
    for x in tup_list:
        tup += (x[1],)
    return tup


print(sort_by_number([(6, 'DV1574'), (4, 'Python'), (5, 'course'), (1, 'Welcome'), (3, 'the'), (2, 'to')]))