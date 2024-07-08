import random
# hungman game
import random
from hungame_word import word_list
chosen_word = random.choice(word_list)
lives = 6
#testing code
#print(f'pssst, the solution in {chosen_word}')
word_len = len(chosen_word)
display = []
for _ in range(word_len):
    display += "_"
end_of_game = False
while not end_of_game:
    guess = input("guess a letter").lower()
    if guess in display:
        print(f"you've already guessed {guess}")

    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"you guessed {guess},that's not in word, you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("you won")
    from hungame_art import stages
    print(stages[lives])














