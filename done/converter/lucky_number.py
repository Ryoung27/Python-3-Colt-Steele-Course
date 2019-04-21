from random import randint

choice = randint(1,10)

if choice == 7:
    print("Lucky")
else:
    print("Not lucky")

num = randint(1,1000)

if num % 2 == 0:
    print("Even")
    print(num)
else:
    print("Odd")
    print(num)