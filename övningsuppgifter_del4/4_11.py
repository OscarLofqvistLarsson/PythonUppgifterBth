my_list = list(range(10))
square_list = list(map(lambda x:x**2, my_list))
filtered_list = list(filter(lambda x:x > 10 and x < 80, square_list))
print(filtered_list)