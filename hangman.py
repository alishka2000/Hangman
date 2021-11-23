import random

def print_0_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |         ")
    print("  |         ")
    print("  |         ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_1_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      o  ")
    print("  |         ")
    print("  |         ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_2_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      o  ")
    print("  |      |  ")
    print("  |      |  ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_3_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      o  ")
    print("  |     /|  ")
    print("  |      |  ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_4_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      o  ")
    print("  |     /|\\")
    print("  |      |  ")
    print("  |         ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_5_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      o  ")
    print("  |     /|\\")
    print("  |      |  ")
    print("  |     /   ")
    print(" /|\\       ")
    print("/ | \\      ")

def print_6_mistakes():
    print("  |------|- ")
    print("  |      |  ")
    print("  |      o  ")
    print("  |     /|\\")
    print("  |      |  ")
    print("  |     / \\")
    print(" /|\\       ")
    print("/ | \\      ")

def print_game_status():
    if mistakes == 0:
        print_0_mistakes()
    elif mistakes == 1:
        print_1_mistakes()
    elif mistakes == 2:
        print_2_mistakes()
    elif mistakes == 3:
        print_3_mistakes()
    elif mistakes == 4:
        print_4_mistakes()
    elif mistakes == 5:
        print_5_mistakes()
    elif mistakes == 6:
        print_6_mistakes()

    print("Word: ", end='')
    for element in guesses:
        print(f"{element} ", end='')
    print(f"\nYou have {remaining_guesses} guess(es) left")
def play_again():
    print("Do you want to play again? (yes/no)")
    return input().lower().startswith('y')

words = ["artist", "writer", "apple", "banana", "thief", "animal", "kazakh", "polish", "russian", "jeans"]
guesses = []
remaining_guesses = 6
mistakes = 0
word_index = random.randint(0, len(words)-1)
word = words[word_index].upper()

for i in range(len(word)):
    guesses.append('_')

game_over = False

while not game_over:
    print_game_status()
    letter = '';

    user_input = input("Please enter a letter:\n")

    if not user_input or user_input[1:] or user_input not in 'abcdefghijklmnopqrstuvwxyz':
        print("That's not a valid input. Please try again")
    elif user_input == letter:
        print("You shouldn't type same words")
    else:
        letter = user_input[0].upper()
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guesses[i] = letter
            if '_' not in guesses:
                game_over = True
        else:
            print("Sorry, that's not part of the word")
            remaining_guesses -= 1
            mistakes += 1
            if mistakes == 6:
                game_over = True

if mistakes == 6:
    print_game_status()
    print(f"YOU LOSE! The word was {word}. TRY AGAIN LATER)))")
else:
    for i in range(4):
        print("\U0001f389 \U0001F38A \U0001F388 ", end='')
    print()
    print("CONGRATZ, YOU WON!!!")
    print(f"The word was {word}")

if game_over:
    if play_again():
        guesses = []
        remaining_guesses = 6
        mistakes = 0
        game_over = False
        word_index = random.randint(0, len(words) - 1)
        word = words[word_index].upper()

        for i in range(len(word)):
            guesses.append('_')
    else:
        pass
