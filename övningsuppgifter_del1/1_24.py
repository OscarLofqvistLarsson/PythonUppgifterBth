year = int(input("Year to check"))

if year % 4 == 0 and year % 100 != 0:
    print(year,"is leap year")

elif year % 4 == 0 and year % 100 == 0 and year % 400 ==0:
    print(year,"is leap year")
else:
    print("is not a leap year")