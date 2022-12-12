import random
import string

# create a list of letters 
alphabet = string.ascii_lowercase
# print(alphabet)

# create a list of words
word_list = ['raspberry', 'peach', 'blackberry', 'grape', 'plum']
print(word_list)

# select a random word from the list
word = random.choice(word_list)
print(word)

# get user input and verify it
print('Please enter a single letter: ')
guess = input()

if len(guess) == 1 and guess.isalpha() == True:
    print(guess)
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
