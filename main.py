import random

score = 0
# truns the game into number
list = ['rock', 'paper', 'scissors']
# randomliying chosing the numbers
pdf = random.sample(list,1)
# guess from user
user_guess = input("what is your guess")
# seeing if got it corret
try:
    user_guess == pdf
except:
    print("won")
else:
    print("you failed")
    print(pdf)