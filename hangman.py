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
    for attempt in range(attempts):
        char = input("Guess a letter. \n").lower()
        if char in word:
            print(f"Correct! {char} is in the word. ")
            guessList.append(char)
            guesses = ' '.join(map(str, guessList))
            print(f"Your correct guesses so far are: {guesses}.")
        else:
            print("Wrong!")
            print(f"Your correct guesses so far are: {guesses}.")
    guessWord = input("Would you like to guess the word? \n").lower()
    if (guessWord == word):
        print("Correct, you win! \n")
        score += 1
    else:
        print("You lose.")
    rematch = input("Would you like to play again? y/n \n").lower()
    if (rematch == "y"):
        playGame()
    else:
        print("Okay, goodbye.")
        return

playGame()