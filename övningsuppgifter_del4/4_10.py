import math

# print(list(map(len, ["I", "love", "Python"])))

fibonacci_list =[]
for i in range(13):
    a = (math.pow((1+math.sqrt(5)),i) - math.pow((1 - math.sqrt(5)),i))/(math.pow(2,i)*math.sqrt(5))
    fibonacci_list.append(int(a))

print(fibonacci_list)
fibonacci_cubic = list(map(lambda x:x**3, fibonacci_list))
print(fibonacci_cubic)