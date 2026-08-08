import random as rnd

from Day7.Words import word_list
from Day7.Hangma_stage import hangman_stages

chosen_word = rnd.choice(word_list)

lives = 6

display = ["_" for _ in chosen_word]

guessed_letters = []

print("🎮 Welcome to Hangman!")
print(hangman_stages[0])
print(" ".join(display))

game_over = False

while not game_over:

    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:

        for position in range(len(chosen_word)):

            if chosen_word[position] == guess:
                display[position] = guess

        print("✅ Correct!")

    else:

        lives -= 1

        print(f"❌ '{guess}' is not in the word.")
        print(f"Lives Remaining: {lives}")

    print("\nWord:")
    print(" ".join(display))

    # Print current Hangman stage
    print(hangman_stages[6 - lives])

    if "_" not in display:
        game_over = True
        print("\n🎉 You Win!")

    if lives == 0:
        game_over = True
        print("\n💀 You Lose!")
        print(f"The word was: {chosen_word}")