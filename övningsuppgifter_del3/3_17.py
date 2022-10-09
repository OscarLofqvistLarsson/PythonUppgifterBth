def list_2_dict(lst):
    dict = {}
    counter = -1
    for element in lst:
        counter +=1
        if element != 0:
            dict[counter] = element

    return dict

print(list_2_dict([1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4]))