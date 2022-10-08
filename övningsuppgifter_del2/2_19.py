def extend_each(my_item, my_list):
    sub_list = [my_item]
    for i in range(len(my_list)):
        my_list[i] += sub_list
    return my_list

print(extend_each("oo",[["kangar"], ["z"], ["f"]]))