import random
name = input(int("hello whats your name"))
number = random.randint(1,9):
print("I am thinking of a number between 1 and 9",name)
while numberofguesses<5:
    guess=input(int("take a guess"))
    numberofguesses=numberofguesses+1
    if guess < number:
        print ("you guessed too low")
    if guess > number:
        print ("you guessed too high")
    else:
        print ("you got it right")