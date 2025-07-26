import random
def guess_the_word():
    words = ['apple', 'python', 'chair', 'water', 'hello','mango','Java','Datascience','Avacado','Mobile','Laptop']
    word = random.choice(words)  # pick a random word
    guessed = ['_'] * len(word)  # show blanks for each letter
    attempts = 6  # you can change the number of chances
    guessed_letters = []

    print("Welcome to Guess the Word!")
    print("You have", attempts, "attempts to guess the word.")
    print("Word:", ' '.join(guessed))

    while attempts > 0 and '_' in guessed:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guewss.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", attempts)

        print("Word:", ' '.join(guessed))

    if '_' not in guessed:
        print("Congratulations! You guessed the word:", word)
    else:
        print("You ran out of attempts. The word was:", word)

# Run the game
guess_the_word()
