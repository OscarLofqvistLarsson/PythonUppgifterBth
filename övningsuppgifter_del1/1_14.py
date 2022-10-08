def hypotenuse(a_side,b_side):
  import math
  c_side = math.sqrt((a_side * a_side) + (b_side * b_side))
  return round(c_side,2)

print(hypotenuse(10,16))