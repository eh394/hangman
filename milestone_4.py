import random

word_list = ['raspberry', 'peach', 'blackberry', 'grape', 'plum']

class Hagman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word_guessed))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []


        






# create a list of words

# print(word_list)

# select a random word from the list
# word = random.choice(word_list)
# print(word)

# get user input and verify it
# def check_guess(guess):
#     guess = guess.lower()
#     if guess in word:
#         print(f'Good guess! {guess} is in the word.')
#     else:
#         print(f'Sorry, {guess} is not in the word. Try again.')

# def ask_for_input():
#     print('Please enter a single letter: ')
#     guess = input()
#     while True:
#         if len(guess) == 1 and guess.isalpha():
#             break
#         else:
#             print('Invalid letter. Please enter a single alphabetical character.')
#             guess = input()
    
#     check_guess(guess)
#     return guess
    
# ask_for_input()
    



