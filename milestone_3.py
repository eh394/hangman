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
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

def ask_for_input():
    print('Please enter a single letter: ')
    guess = input()
    while (len(guess) != 1 or guess.isalpha() == False) == True:
        print('Invalid letter. Please enter a single alphabetical character.')
        guess = input()
    guess = guess
    check_guess(guess)

ask_for_input()





