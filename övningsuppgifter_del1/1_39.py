import math

number_1 = int(input("enter number in series for Fibonacci"))

value_from_number = (math.pow((1+math.sqrt(5)),number_1) - math.pow((1 - math.sqrt(5)),number_1))/(math.pow(2,number_1)*math.sqrt(5))

print(value_from_number)

for i in range(1,100):
    a = (math.pow((1+math.sqrt(5)),i) - math.pow((1 - math.sqrt(5)),i))/(math.pow(2,i)*math.sqrt(5))
    print(a)