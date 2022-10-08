def matrix_dimensions(matrix):
    count_lst = 0
    count_int = 0

    for num in matrix:
        if isinstance(num,list):
                count_lst += 1
        for x in num:
            if isinstance(x,int):
                count_int += 1
    if count_int == 6 and count_lst ==2:
        return print("this is a 2x3 matrix")
    if count_int == 6 and count_lst ==3:
        return print("this is a 3x2 matrix")
    else:
        return print("this is not a valid matrix")


matrix_dimensions([ [1,1,1],[1, 2, 4]])