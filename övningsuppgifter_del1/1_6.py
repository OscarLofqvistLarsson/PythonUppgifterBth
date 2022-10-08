

year = int(input("What year where you born?"))
mon = int(input("In what month(number)?"))
day = int(input("What day?"))

if year > 2022:
    print("Doubt")
else:
    year = 2022 - year
    print("You are/ will be", year , "years old!")