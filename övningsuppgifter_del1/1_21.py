def is_isosceles(x,y,z):

    if x > 0 and y > 0 and z > 0:

        if x == y or x == z or z == y:
            return True
        else:
            return False

    else:
        print("Something is wrong with the inputs")

print(is_isosceles(2,1,2))