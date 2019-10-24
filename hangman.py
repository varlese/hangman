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
    word = random.choice(words);
    return(word)

def getWordLength():
    word = selectWord()
    wordLength = len(word)
    return wordLength

def guessWord():
    word = selectWord()
    attempts = getWordLength() + 2
    guesses = []
    for attempt in range(attempts):
        char = input("Guess a letter. \n")
        if char in word:
            print(f"Correct! {char} is in the word. ")
            guesses.append(char)
            print(f"Your correct guesses so far are {guesses}.")
        else:
            print("Wrong!")

guessWord()