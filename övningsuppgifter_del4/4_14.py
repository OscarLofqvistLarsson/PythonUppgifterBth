num_list = [1, 2, 3, 8, 10,13,14,141,4,456,454,7,56,78,78,67,353,5,345,345,2,334,23,4,23,4,234,234,2,34,234,534,6,47,45,3,5,34,5,3,5,34,5]

def above_average(list):
    return [i for i in list if i > (sum(list)/len(list))]

print(above_average(num_list))