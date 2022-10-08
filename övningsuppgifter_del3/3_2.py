def all_pair(my_list):
    num_list = []
    num2_list = []
    for x in my_list:
        for y in my_list:
            num2_list.append(y)
            num_list.append(x)

    res = list(zip(num_list, num2_list))
    return res

print(all_pair([1,2,3]))
