def add_first_and_last(num_list):
    if len(num_list) > 1:
        result = num_list[0] + num_list[-1]
        return result
    else:
        return num_list[0]

print(add_first_and_last([2, 7, 4, 3]))