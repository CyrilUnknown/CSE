import random
the_list = ["Vapor", "Edison", "Wonder", "Microsoft", "Configure", "Adventure",
            "Fjord", "Master", "Waves", "Burger"]
letters_guessed = []
the_word = random.choice(the_list)
Guesses = 6
guess = ""
word = list(the_word)
hidden_word = list(the_word.lower())
length_words = len(word)
if the_word == "Microsoft":
    length_words -= 1

for i in range(len(word)):
    if word[i] not in letters_guessed:
        word.pop(i)
        word.insert(i, "?")

while Guesses > 0 and length_words > 0:
    print("".join(word))
    print("You have %d guesses left" % Guesses)
    guess = input("Guess a letter: ")
    if len(guess) > 1:
        print()
    else:
        if guess == "":
            print("You didn't guess anything")
        else:
            if guess in letters_guessed:
                print("You already guessed that!")

            else:
                if guess.lower() in hidden_word:
                    print("You guessed a letter!")
                    length_words -= 1
                letters_guessed.append(guess.lower())
                letters_guessed.append(guess.upper())
                word = list(the_word)
                for i in range(len(word)):
                    if word[i] not in letters_guessed:
                        word.pop(i)
                        word.insert(i, "?")
                if guess.lower() not in hidden_word:
                    print("Incorrect! Try Again!")
                    Guesses -= 1
