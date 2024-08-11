import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
print(hangman_art.logo)
# print(f"Passt, the solution is {chosen_word}")
display = []
for _ in chosen_word:
    display.append("_")

end_of_game = False
while not end_of_game:
    guess = input("Make a word guess ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    if guess not in chosen_word:
        print(f"{guess} not in chosen word")
        lives -= 1
        
        if lives == 0:
            print("You lose!!!")
            end_of_game = True
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")
    print(hangman_art.stages[lives])
