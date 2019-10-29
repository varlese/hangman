import random

words = ["brazil",
         "united",
         "foreign",
         "france",
         "travel",
         "photograph",
         "memory",
         "suitcase"]

def selectWord():
    word = random.choice(words)
    return(word)

def playGame():
    word = selectWord()
    attempts = len(word) + 2
    guessList = []
    guesses = " "
    for attempt in range(attempts):
        char = input("Guess a letter. \n").lower()
        if char.isalpha():
            if char in word:
                guessList.append(char)
                guesses = ' '.join(map(str, guessList))
                print(f"Correct! {char} is in the word. " +
                      f"Your correct guesses so far are: {guesses}.")
                if len(word) == len(guessList):
                    print(f"You\'ve guessed all of the letters!")
                    break
            else:
                print("Wrong!")
        else:
            print(f'That\'s not a letter! Try again.')
    guessWord = input(f"Would you like to guess the word? \n").lower()
    if (guessWord == word):
        print("Correct, you win!")
    else:
        print("You lose.")
    rematch = input("Would you like to play again? y/n \n").lower()
    if (rematch == "y"):
        playGame()
    else:
        print("Okay, goodbye.")
        return

playGame()