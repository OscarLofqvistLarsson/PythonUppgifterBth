min_value = int(input("min value"))
max_value = int(input("max value"))
n = int(input("divider"))



a = 0
for i in range(min_value, max_value):
    if i % n == 0:
        a += i
print(a)