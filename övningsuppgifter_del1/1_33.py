import math
start_value = int(input("start value?"))
interest = float(input("interest?"))
years = int(input("years?"))

total_value = start_value * math.pow(interest, years)

print(total_value)