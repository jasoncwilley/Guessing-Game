from random import randint

guess_number = 0

print("Hello! Welcome to the Mystery Number Guessing Game, What is your Name?")
#player1 = input()
#player1 = "jason"
mystery_number = (randint(0, 100))
print("Let's get the game statred Jay.")
number_of_rounds = input("How many rounds would you like to play?") + 1
print("I am thinking of a number between 0 and 100.")

while guess_number < number_of_rounds:
    print("Jay what is the mystery number?")
    guess = input()
    guess = int(guess)
    guess_number = guess_number
    guess_number = int(guess_number) + 1
    if guess == mystery_number:
        print("That's correct, Are you a psycic?")
    elif guess > mystery_number:
        print("Close but No Cigar, the mystery number is lower than that.")
    elif guess < mystery_number:
        print("Close but No Cigar, the mystery number is greater than that.")
if guess == mystery_number:
    mystery_number = str(mystery_number)
    print("That's correct, Are you psycic or just lucky?")
if guess != mystery_number:
    mystery_number = str(mystery_number)
    print("You are out of guesses, the number I was thinking of was")
    print(mystery_number)
