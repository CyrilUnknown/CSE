import random
guesses = 5
playing = True
random_number = random.randint(1, 10)
while guesses > 0 and playing:
    guesses -= 1
    number_guessed = int(input("Guess number 1-10 get the number or you loss?"))
    if number_guessed > random_number:
        print("Guess Lower")
    elif number_guessed < random_number:
        print("Guess Higher")
    elif number_guessed == random_number:
        playing = False
if number_guessed == random_number:
    print("You Won Hooray!!!!!")
