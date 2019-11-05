# Author: 	azmathias Stuperuser Ltd.
# Purpose: 	Guess the number game. User has 5 attempts to guess a number between 1 and 20. 
# ToDo: 	Add Error Handling


import random

print('Hello. What is your name?')
name = input()
secNum = random.randint(1,20)
print("\nWell, " + name + ", I'm thinking of a number between 1 and 20")

# Player has 5 guesses
for guessTaken in range(1,6):
	print('Take a guess.')
	guess = int(input())
	if guess < secNum:
		print('Your guess is too low.')
	elif guess > secNum:
		print('Your guess is too high')
	else:
		break
if guess == secNum:
	print('Well done ' + name + '! You guessed correctly')
else:
	print('No. The number I was thinking of was ' + str(secNum))
