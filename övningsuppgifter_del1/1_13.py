def percent(value, total):
  p_value = value / total
  p_value = p_value * 100
  return int(p_value)

print(percent(46,90))