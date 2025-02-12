import random
from hangman_words import *
from hangman_art import *
print(logo)

chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')
display = []
for item in chosen_word:
    display += "_"
print(display)


display_length = len(display) 
end_of_game = False
lives = 6
# guess_list = []
while not end_of_game:
    
    guess = input("guess a letter.").lower()
    
    # if guess in guess_list:
    #     print(f"you've already guessed the letter {guess}")
    # if guess not in guess_list:
    #     guess_list += guess
    if guess in display:
        print(f"you've already guessed the letter {guess}")


    for position in range(display_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
            
            
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win.")
    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word.You lose a life.")
        print("_ _ _ _ _ _ _ _ _ _ _ ")
        lives -= 1
        tackle = stages[lives]
        print(tackle)
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    



