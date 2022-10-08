def unit(int_num):                          #can´t import my files
  return int_num % 10

def ten(int_num):
  return int_num // 10


def swap_units_and_tens(int_num):
    return int_num + 9 * (unit(int_num) - ten(int_num))

print(swap_units_and_tens(42))