#if n > 10:
#    if n > 100:
#        if n < 1000:
#            print(n)
#        else:
#            if n < 1001:
#                print('Pretty large')
#            else:
#                print(n)
#    else:
#        if n == 11:
#            print(n)
#        else:
#            if n == 10:
#                print('10!')
#            else:
#                print(n)
#else:
#    if n < 0:
#        print('Below zero')
#    else:
#        print(n))

import random
n = random.randint(-250,1250)

if n > 10 and n > 100 and n < 1000:
    print(n)
if n < 1001:
    print("pretty large")
if n > 1001:
    print(n)
if n == 10:
    print("10!")
if n == 11:
    print(n)
if n < 0:
    print("below zero")
    print(n)

