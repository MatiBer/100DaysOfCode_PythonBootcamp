# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import os
import hangman_art
import hangman_words

#word_list = ["samolot", "laptop", "szkola"]
chosen_word = random.choice(hangman_words.word_list)
word_len = len(chosen_word)
lives = 6

print(hangman_art.logo)

display = []
for letter in range(word_len):
    display += "-"
print(display)

end_of_game = False

while not end_of_game:
    # os.system('cls')
    guess = input("Guess a letter: ").lower()



    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_len):
        letter = chosen_word[position]
        # print(f"Current possition: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")


    if "-" not in display:
        end_of_game = True
        print("You win")

    print(hangman_art.stages[lives])