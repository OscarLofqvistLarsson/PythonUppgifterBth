import random
min_value = int(input("min value of guess"))
max_value = int(input("max value of guess"))

random_number = random.randint(min_value,max_value)
print("guess an number between", min_value,"and",max_value)
guess = int(input())
guesses = 0

if guess < max_value and guess > min_value:
    while guess != random_number:
        if guess < random_number:
            print("higher")
            guesses += 1
            guess =  int(input("guess again"))
        if guess > random_number:
            print("lower")
            guesses += 1
            guess =  int(input("guess again"))


    if guess == random_number:
        print("correct after", guesses)

    else:
        print("something went wrong, try again" )
else:
    print("between", min_value,"and",max_value)