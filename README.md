# MILESTONE 2 CODE

Milestone 2 code executes the following steps:
(1) creates a list of random words
(2) uses python random module to select a random word from that list
(3) takes user input, to be given as a single letter
(4) verifies whether user input is valid and prints a suitable message to that effect

# MILESTONE 3 CODE
Milestone 3 code is based on Milestone 2 code and executes the following steps:
(1) creates a list of random words
(2) uses python random module to select a random word from that list
(3) contains a function called ask_for_input which verifies whether user input is valid and prints a suitable message to that effect. The function uses a while loop with condition True which runs until the user input is considered valid. The function also implements another function written in a separate block of code called check_guess which verifies whether this letter is contained within a randomly generated word in step (2) and once again prints message to that effect. The function returns the user guess.

# MILESTONE 4 CODE
Milestone 4 code creates a class called Hangman. The constructor takes 3 no. arguments: self (instance of a class itself), word_list which stands for a list of words that will be used in the game, and num_lives which is set as default argument with a value of 5. The num_lives stands for a number of lives or tries that a player will get to win or lose the game.

Within body of the constructor, a number of instance attributes are defined. Namely, these are:
word: a word randomly selected from the word_list using python module random; this is a string
word_guessed: a list equal in length to the string word, but with an underscore string '_' at each index position
num_letters: number of unique letters in word; this is derived using set() function
num_lives: as per above, this is set to default value of 5, but can be overwritten when creating an instance
word_list: as explained above
list_of_guesses: initialised as an empty list; throughout a game, guesses of a player will be appended to this list to store letters that were already attempted by the player

The class contains two methods in addition to the constructor: check_guess and ask_for_input. check_guess takes two arguments: self and guess. guess it then reasigned to guess.lower() to elimitate issues with lower / uppercase. The function then execuses an if statement. The if condition runs through a for loop comparing the guess against each index of a string word and where they match, updating word_guessed with that guess at a corresponding index. It then also reduces the num_letters by one, indicating that one unique letter has been guessed / allocated. The else statement, on the other hand, deals with a condition where the guess is incorrect and simply prints a message for the user to the console. Outside of the if else statements the guess is appended to the list_of_guesses to store the letter user already attempted to avoid repetition.

The ask_for_input() method only takes self as an argument. The method executes a while loop with condition True. It uses input() function to ask for user input (aka guess) and assign it to a variable named guess.  Then the while loop runs through an if elif else statement. if statement checks whether input is an alphabetical character. elif checks if the guess is already in list_of_guesses and alerts the player. Finally, else statement (i.e. with the two conditions above false, i.e. correct input by the user) calls the check_guess method.

# MILESTONE 5 CODE
Function play_game has been added to the code. The function takes one parameter word_list. Inside the function instance of the Hagman class is created and assigned to an object called game. Two arguments are passed onto the class, word_list as well as num_lives set to 5. The function then executes a while True loop with if, elif and else statements. If statement checks if num_lives, i.e. number of guesses / tries left is equal to zero, if this statement is True, a message letting the player know they lost is printed. elif statement checks if num_letters is larger than 0, i.e. whether there are still letters that need to be guessed. If this is true, the game continues so the ask_for_input method is called on the instance of the class. else statement deals with the remaining scenario, i.e. when player won and prints the message to that effect. Both if and else statement include a break clause to ensure the while loop does not run idenfinitely.