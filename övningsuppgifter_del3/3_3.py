def unordered_pairs(my_list):
    result = []
    for i in range(len(my_list)):
        for k in range(i, len(my_list)):
            result.append((my_list[i], my_list[k]))
    return result

print(unordered_pairs([1,2,3]))