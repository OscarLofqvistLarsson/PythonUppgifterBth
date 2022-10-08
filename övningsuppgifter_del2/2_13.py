start_list = [5, 3, 1, 2, 4]
square_list = []

for num in start_list:
    square = num * num
    square_list.append(square)

square_list.sort()
print(start_list, square_list)