import nltk
import random
from nltk.corpus import words

nltk.download('words')
word_list = words.words()


def word_guess():
    try:
        word = random.choice(word_list)
        count = 0
        num_of_guess = len(word) + 2
        wrong_guesses = 0
        guessed = set()
        current_state = ['_' for _ in word]

        reveal_index = random.randint(0, len(word) - 1)
        revealed_letter = word[reveal_index]
        guessed.add(revealed_letter)
        current_state[reveal_index] = revealed_letter

        print(f"The word is an {len(word)} letter word ")

        print("One letter is revealed")

        print("Current state of the word: {}".format(' '.join(current_state).upper()))

        while count < num_of_guess and wrong_guesses < 3:

            user = input(" enter your guess: ")
            if user.isalpha() and len(user) == 1:
                if user in guessed:
                    print('already guessed')
                elif user in word:
                    print("nice")

                    guessed.add(user)
                    for index, letter in enumerate(word):
                        if letter == user:
                            current_state[index] = user
                    wrong_guesses = 0
                else:
                    print("Wrong guess")
                    wrong_guesses += 1
                    guessed.add(user)

                count += 1
                print("current state of the word: {}".format(' '.join(current_state).upper()))

            else:
                print("please only letters is allowed")

            if all(letters in guessed for letters in word):
                print("congratulations! you guessed the word '{}' You won.".format(word))
                break



        else:
            if wrong_guesses >= 3:
                print("Sorry, you made three consecutive wrong guesses '{}'".format(word).upper())
            else:
                print(" sorry: you are out of move")


    except KeyboardInterrupt:
        exit()


word_guess()
