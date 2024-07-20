import random

def word_guessing_game():
    words = ["lemon", "mango", "banana", "apple"]
    player_name = input("Enter your name: ")
    print(f"Hi {player_name}, let's start the game!\n")
    print("*** Word Guessing Game ***\n")
    random_word = random.choice(words)
    guessed_letters = set()

    while True:
        display_word = ''.join([char if char in guessed_letters else '_' for char in random_word])
        print(f"Word: {display_word}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        guessed_letters.add(guess)

        if guess in random_word:
            print("Correct guess!")
        else:
            print("Incorrect guess!")

        if set(random_word) == guessed_letters:
            print(f"Congratulations, {player_name}! You've guessed the word: {random_word}")
            break

    print(f"Sorry, {player_name}, you're out of attempts. The word was: {random_word}")

if __name__ == "__main__":
    word_guessing_game()
