import numbers

def is_number(item):
    return isinstance(item, numbers.Number)


def sum_numbers(any_list):
    for item in any_list:
        if is_number(item) == False:
            any_list.remove(item)
        if is_number(item) == True:
            return sum(any_list)
    return sum(any_list)


print(sum_numbers(["a", 1, "b", 2, [["b", 4], 2], 3]))
print(sum_numbers([1, 2, 3.2, 4, 5]))