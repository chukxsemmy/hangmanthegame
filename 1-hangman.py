import random;

wordList = ['wares',
    'soup',
    'mount',
    'extend',
    'brown',
    'expert']

def getWord():
    word = random.choice(wordList)
    return word.upper()

def play(word):
    wordCompletion = "-" * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 6
    print("Welcome To Chukxies Hangman")
    print(display_hangman(tries))
    print(wordCompletion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessedLetters.append(guess)
            else:
                print("Nice one", guess, "is the word")
                guessedLetters.append(guess)
                word_as_list = list(wordCompletion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                wordCompletion = "".join(word_as_list)
                if "_" not in wordCompletion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                print("You already guessed the word..., sips wine (:")
            elif guess != word:
                print(guess, "is not in the word")
                tries -= 1
                guessedWords.append(guess)
            else:
                guess = True
                wordCompletion = word

        else:
            print("Not a valid word or letter")
        print(display_hangman(tries))
        print(wordCompletion)
        print("\n")
    if guessed:
        print("Your Shoe shine, you guessed the word")
    else:
        print("Your face no show cus you ran out of tries. Heres the word " + word + " Try again abeg" )


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = getWord()
    play(word)
    while input("Play again? (Y/N)").upper == "Y":
        word = getWord()
        play(word)


if __name__ == "__main__":
    main()
