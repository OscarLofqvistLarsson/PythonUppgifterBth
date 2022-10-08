for i in range(26):
    print(i)
print("_____________")

for i in range(25,0,-1):
    print(i)
print("_____________")

for i in range(31):
    if i % 2 == 0:
        print(i)
print("_____________")

a = 0
for i in range(37,150):
    a+= i
print(a)
print("_____________")

min_value = int(input("numbers to sum between start with lower"))
max_value = int(input("and the higher"))
b = 0
for i in range(min_value,max_value):
    b += i
print(b)
print("_____________")