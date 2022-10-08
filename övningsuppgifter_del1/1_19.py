def  max2(num1, num2):

    if num1 < num2:
        return num2
    if num1 > num2:
        return num1
    else:
        return num1, 'och', num2 ,'är lika stora'

print(max2(2,2))