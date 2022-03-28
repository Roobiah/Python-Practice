
import random
from hangman_art import stages, logo
from hangman_words import word_list

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print("Welcome to the hangman!")
print(f"{logo}")

display = []
for letter in range(word_length):
    display += '_'
print(display)

while not end_of_game:
    guess = input("Guess a letter: \n").lower()
    if guess in display:
        print(f"You've guessed {guess} before.")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. You've lost a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose")
        print(stages[lives])
    if '_' not in display:
        end_of_game = True
        print("you won")
    print(display)
