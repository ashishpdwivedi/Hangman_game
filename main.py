# Welcome to Hangman game

print("Welcome to Hangman Game......")

# Importing the Modules

import random

# Importing Hangman Words and Logo

from hangman_art import logo,stages

from hangman_word import  word_list

# Step 1  - Creating random method to choose the word and Blank "_" letter

chosen_word = random.choice(word_list)

print(chosen_word)

# Creating the Placeholder for Blank words

print(logo)

placeholder = ""

world_len  = len(chosen_word)

for position in range(world_len):
    placeholder += "_"



# Step 2 - Creating the Game Logic

game_over = False

correct_letters =[]

# We will give Max 6 Chances to Guess the Word
lives = 6



while not game_over:
    guess = input("Please Guess the Word : ")
    print(f"You have {lives} lives left")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
            print(f"You have already guessed {guess}")

        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"word to guess {display}")

    # Now We will set the Logic of Chances
    if guess not in chosen_word:
        lives -= 1
        print(f"Your Guess letter {guess} is not in the word")
        print(f"You have {lives} lives left")

        if lives == 0:
            game_over = True
            print("Oops, you have not Guessed Correct Word")
            print("************** You Lose ******************")

    # Now Creating the Logic of Game over

    if "_" not in display:
        game_over = True
        print(f"You have Sucessfully Guessed {guess}")
        print("***************** You Win *******************")


   # Now Printing the Hangman Stages
    print(stages[lives])





