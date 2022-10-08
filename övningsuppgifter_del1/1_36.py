c = 0
for i in range(0,2000):
    if i % 3 == 0 or i % 7 ==0:
        c += i
print(c)