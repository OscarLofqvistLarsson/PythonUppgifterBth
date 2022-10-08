#if n > 0:
#    if n > 100:
#        print('Big!')
#    else:
#        if n <= 50:
#            print('Medium')
#        else:
#            print('A little larger')
#else:
#    print('Tiny') )

import random
n = random.randint(-250,250)

if n > 100:
    print("Big!")
if n <= 50 and n > 0:
    print("mid")
if n >50 and n < 100:
    print("slightly large")
if n < 0:
    print("tiny")
