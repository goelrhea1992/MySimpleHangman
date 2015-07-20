import random
import time
import string

#hangman game

WORDLIST_FILENAME = "words.txt"

"""
	loadWords() function returns a list of valid words. Words are strings of lowercase letters.
	Depending on the size of the word list, this function may
	take a while to finish.
"""

def loadWords():
	print "Loading word list from file..."
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r', 0)
	# wordlist: list of strings
	wordlist = []
	for line in inFile:
		wordlist.append(line.strip().lower())
	print "  ", len(wordlist), "words loaded."
	return wordlist

wordList = loadWords()

"""
	getScore() function returns the score of the word correctly guessed by the user. The final score of the word is calculated as twice the length of 		the word minus the no. of chances he/she took! So, the longer the word, more is the score!	
"""

def getScore(finalWord,numOfGuesses):
	score = len(finalWord) * 2 - numOfGuesses + 1
	return score

"""
	currentStatus() function returns a string, the current progress made by the user, depending upon the so far success and the currently input guess.
"""

def currentStatus(currentWord,finalWord,userGuess):
	temp2 = ""
	for i in range(len(finalWord)):
		if userGuess == finalWord[i]:
			temp2 = temp2 + userGuess
		elif (currentWord[i] >= 'a' and currentWord[i] <= 'z'):
			temp2 = temp2 + currentWord[i]
		else:
			temp2 = temp2 + '*'
	return temp2

"""
	The remaining code snippet generates a random word from the wordList and prints the allowed number of guesses, which are 3 more than the length of the word. It then prompts for the input from the user.
	Depending upon the user input, it either exits the program, or checks for the validity of the character input.
	If the input given by the user is valid, and is a correct guess, the progress is updated and displayed.
	If the user makes an incorrect guess, the number of chances left decreases and the user is prompted for another input.
	If the user is able to guess the word correctly, within the allowed number of guesses, the score is calculated in accordance with the getScore 	function and displayed.
	Otherwise the user scores 0 points. Total score is displayed. The user is then prompted for whether he wants to play again or wants to quit.
	
"""

ans='y'
while ans is 'Y' or ans is 'y':
	# Seeding and finding out the random word from the wordList
	random.seed(time.time())
	x = random.randint(0, len(wordList) - 1)
	finalWord = wordList[x]
	currentWord = ""
    
	print "\nGuess the hidden word: "
	currentWord = '*' * len(finalWord)
	for i in range(len(finalWord)):
		print currentWord[i],

	soFar = ""
	allowedGuesses = 3 + len(finalWord)
	incorrectGuesses = allowedGuesses
	totalScore = 0
	while currentWord != finalWord and incorrectGuesses > 0:
		print "\nYou can make %d guesses now" % incorrectGuesses
		userGuess = raw_input("\nPlease input ONE letter or 'exit' to quit: ")
		userGuess = userGuess.lower()
		
        #checking to see if the user wants to exit or guess a character
		if userGuess == "exit":
		        break
		if len(userGuess) > 1:
			print "Don't cheat!"
			continue
		if userGuess.isdigit() == True:
			print "You've entered a numeral!"
			continue
		if userGuess in finalWord:
			print "Yes that letter is in the word!"
			currentWord = currentStatus(currentWord, finalWord, userGuess)
			print "The hidden word now is: "
			print " ".join(currentWord.upper())
		else:
			print "Im sorry that letter is not in the word."
			incorrectGuesses -= 1
			print "Your progress so far: "
			print " ".join(currentWord.upper())
		
	if userGuess == "exit":
		break
	elif currentWord == finalWord:
		numOfGuesses = allowedGuesses - incorrectGuesses
		print "\n\nCongratulations..."
		print "You guessed the word correctly making %d incorrect guesses!" % numOfGuesses
		print "The word is: ", finalWord.upper()
		score = getScore(finalWord, numOfGuesses)
		print "You scored %d points for guessing this word correctly!" % score
		totalScore += score
		print "Your Total Score is: ", totalScore
	elif incorrectGuesses <= 0:
		print "\nSorry! All your chances are over!"
		print "The hidden word was: ", finalWord.upper()
		print "You scored 0 points for this word!"
		print "Your Total Score is: ", totalScore

	ans = raw_input("\nEnter 'Y' or 'y' to play more, or 'exit' to quit: ")

print "\nThank You for playing MyHangman!\n"

#THE END!!
