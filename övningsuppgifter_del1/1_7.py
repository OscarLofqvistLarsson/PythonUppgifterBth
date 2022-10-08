s = int(input("Input seconds"))

h = s // 3600
s = s % 3600

m = s // 60
s =  s % 60

print(h, "hours", m, "minutes" , s , "seconds")
