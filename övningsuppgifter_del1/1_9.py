from opcode import stack_effect


def minus(x_value,y_value):
  s_value = x_value - y_value
  return s_value

print(minus(20,19))