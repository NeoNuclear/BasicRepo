import random
money = 0
userInput = int(input("Enter loop amount: "))
for i in range(userInput):
    money += 1
    money += 12
money += random.randint(1,100)