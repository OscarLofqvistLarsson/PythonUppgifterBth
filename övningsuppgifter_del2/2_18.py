def distribute(my_item, my_list):
    new_list = []
    sublist = [my_item]
    for item in my_list:
        new_list.append(item + sublist)
    return new_list, my_list

print(distribute("oo",[["kangar"], ["z"], ["f"]]))