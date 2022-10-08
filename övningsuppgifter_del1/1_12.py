def bmi(weight, height):
  bmi_value = (weight / (height * height))
  return round(bmi_value , 1)

print(bmi(75,1.80))

