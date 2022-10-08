
n = int(input("n?"))

def test_1(n):
    if n < 0:
        print('Negative')
    elif n < 1000:
        print('Small')
    elif n > 1000:
        print('Large')
    else:
        print('Medium')

def test_2(n):
    if n > 1000:
        print('Large')
    elif n < 1000:
        print('Small')
    elif n < 0:
        print('Negative')
    else:
        print('Medium')


test_1(n)
test_2(n)

#use if instead to get same result