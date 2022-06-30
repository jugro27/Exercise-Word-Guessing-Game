import random

# reads a file and takes all individual words from it
with open("WordsForGame.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))

# randomly chooses the word for the user to guess
alreadyGuessedWords = []
wordToGuess = random.choice(words)
alreadyGuessedWords.append(wordToGuess)
# checks to see if chosen word has already been used and chooses a different word if it has
for wordToGuess in alreadyGuessedWords:
    if wordToGuess in alreadyGuessedWords:
        wordToGuess = random.choice(words)
        print(wordToGuess)
    else:
        continue

def playGameFunc():
    # setting variables to maintain the wins, lossses, guesses, display of the hidden word, and the words/letters guessed list
    wins = 0
    losses = 0
    guesses = 7
    hiddenWord = ['_' for i in wordToGuess]
    wordsLettersGuessed = []
    # running a while loop for when the player still has guesses remaining
    while guesses > 0:
        guess = str(input("Guess either a word or a letter: "))
        # takes away a guess from the 7 the player has each time they enter an input
        guesses = guesses - 1
        # this is determining that the guess is a word based on its length
        if len(guess) > 1:
            if guess == wordToGuess:
                print(f"Answer:{wordToGuess}")
                print("You win!")
                break
            else:
                print("That is not correct, you lost a life and please try again.")
        # this is determining that the guess is a letter based on its length
        if len(guess) == 1:
            # if the letter guessed is in the word, the list is altered to include that letter
            if guess in wordToGuess:
                wordsLettersGuessed = [i for i, letter in enumerate(wordToGuess) if letter == guess]
                
                #replaces the "_" with the correctly guessed letter
                for i in wordsLettersGuessed:
                    hiddenWord[i] = guess
                #if there are no found "_" in the hidden word display, then the word has been guessed
                if '_' not in hiddenWord:
                    print(f"Answer: {wordToGuess}")
                    print("You win!")
                    break
                # if there are still "_", then it has been partially guessed
                else:
                    print(f"You got a letter! This is your progress so far: {hiddenWord}")
            else:
                print("That letter is incorrect.")
    # keeps track of wins and losses
    if guesses==0:
            losses += 1
            playAgain = input("Would you like to play again? (Y/N): ")
            if playAgain == "Y":
                playGameFunc()
            if playAgain == "N":
                exit
    else:
        wins += 1

playGameFunc()