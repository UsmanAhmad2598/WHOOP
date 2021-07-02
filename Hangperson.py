
#Hangperson Game

import random

def print_gallows(num_missed):
    '''
    Make a poor-human's representation of the hangperson gallows.
    Parameter to the function is the number of missed words (7 misses
    means that the player is fully strung up).
    '''
    print()
    print()
    print('       |||========|||')
    if num_missed > 0:
        print('       |||         |')
    else:
        print('       |||          ')

    if num_missed > 1:
        print('       |||         O')
    else:
        print('       |||          ')

    if num_missed > 2:
        if num_missed > 4:
            print('       |||        /|\\')
        elif num_missed > 3:
            print('       |||        /| ')
        else:
            print('       |||        /  ')
    else:
        print('       |||           ')

    if num_missed > 5:
        if num_missed > 6:
            print('       |||        / \\')
        else:
            print('       |||        /  ')
    else:
        print('       |||           ')

    print('       |||')
    print('       |||')
    print('     =================')
    print()

def choose_version(words):
    """ (list) -> list
    Function that accepts the list of words and prompts the user for the version of hangperson
    he/she wants to play and returns the modified/unmodified list of words (according to the version chosen)
    """
    valid=False
    while not valid:                                           #loop that runs until a valid input for version is entered
        version=input("Which version of hangman do you want to play, evil or regular. Enter 'evil' or 'regular': ")
        version=version.lower()                                #input converted to lower case for easy comparison
        if version=="evil" or version=="regular":               
            valid=True
        else:
            print("\nEnter a valid input\n")
            valid=False
    if version=="evil":                                        #if the user chooses to play evil hangman, the list is modified according to that
        words=evil_hangman(words)
    return words                                               #the list is returned

def choose_secret_word(words):
    """ (list) -> str
    Accepts a list of words and returns a randomnly chosen word(secret)
    from that list
    """
    secret = random.choice(words)                              #method to choose a word randomnly from the list 
    return secret

def initialise_guess_state(secret):
    """ (str) -> str
    function that accepts a string(secret) and
    returns a string with as many blank dashes( _ )
    as the number of letters in secret
    """
    current_guess_state=[]                                      #list to store the dashes ( _ )
    for i in range(len(secret)):                                #loop that runs as many times as the letters in secret
        current_guess_state.append("_")                         #during each iteration, a blank dash ( _ ) is added to the list
    return " ".join(current_guess_state)                        #returns the string (join is used to convert list into string with all the elements of list joined by a space in between them)

def check_valid(guess):
    """ (str) -> bool
    Function accepts a string (guess) and returns True if the input is valid(it is a single letter)
    or False if it is not valid, outputting the error message
    """
    if (guess.isalpha()) and (len(guess)==1):                   #condition to check validity of guess input-it should be a single letter.
        return True                                             #If valid, True returned
    else:
        print("Please enter one letter!\n")                     #if the input for guess is not valid, appropriate error message outputted and False returned
        
        return False
def check_duplicate(guess,unique_letters_guessed):
    """ (str,str) -> bool
    Function accepts two strings(guess and string keeping track of unique letters already entered(unique_letters_guessed)
    and returns True or False based on whether the guess input exists in unique_letters_guessed
    meaning that it is a duplicate value-this guess value has been previously entered
    """
    if guess in unique_letters_guessed:                         #condition to check if the current guess has been previously entered 
        print("\nYou have already guessed",guess)                 #if the guess is duplicate(it has been previously entered), error message outputted and True is returned
        return True                                              
    else:
        return False


def new_guess(unique_letters_guessed):
    """ (str) -> str
    function to prompt the user to enter a new guess. It calls check_valid and check_duplicate
    functions to ensure that the input entered is valid and has not been entered previously.
    returns the valid and non-duplicate guess input
    """
    valid=False
    duplicate=True
    while not (valid) or duplicate:                             #loop that runs continuously, prompting user to enter a value for guess, until a valid and non-duplicate value is entered
        guess=input("What is your guess? ")
        guess=guess.upper()                                     #input converted to upper case for easy comparisons
        valid=check_valid(guess)                                #function call to check if the input is valid or not
        duplicate=check_duplicate(guess,unique_letters_guessed) #function call to check if this input for guess has been already entered or not
            
    return guess                                                #a valid, non-duplicate guess is returned
        

def update_guess_state(current_guess_state,guess,secret):
    """ (list,str,str) -> str
    Function that iterates through all the letters of secret and if any matches the current guess,
    the dash (underscore) in current_guess_state at that place is replaced by this letter(guess)
    """
    for i in range(len(secret)):                                #loop to iterate through all the letters of secrets
        if guess==secret[i]:                                    #condition to check if any letter in secret matches the current guess input
            current_guess_state[i]=guess
        
    return " ".join(current_guess_state)                        #the updated current_guess_state list is converted to string( all elements of list are joined) and returned



def update_wrong_attempts(wrong_guesses,guess,secret):
    """ (int,str,str) -> int
    Function to check if the guess is a wrong guess. If it is, function increments the variable
    keeping track of the number of wrong guesses(wrong_guesses) and returns it
    """

    if not (guess in secret):                                   #condition to check if the guess input is a wrong guess(this letter is not a part of the secret word)
        wrong_guesses+=1                                        #if guess is wrong, the variable wrong_guesses(keeping track of number of wrong guesses) incremented by 1

    return wrong_guesses                                        #the updated number of wrong guesses is returned 
def check_attempts_exhausted(wrong_guesses):
    """ (int) -> bool
    Function to check if the user has made 7 wrong guesses, meaning he has lost the game
    """
    if wrong_guesses==7:                                        #condition to check if the number of wrong_guesses has reached 7
        return True
    else:
        return False
def check_win(current_guess_state,secret):
    """ (list,str) -> bool
    function that accepts list of current guess state
    (letters already guessed and empty blanks) and compares it with secret
    and returns true if the entire secret word has been guessed, or otherwise returns false
    """
    current_guess_state=current_guess_state.replace(" ","")
    
    if current_guess_state==secret:                             #condition to compare if the current_guess_state is equal to secret, meaning the entire secret word has been guessed
        return True                                             #if the entire secret word has been guessed, true is returned
    else:
        return False                                            #if the entire secret word has not been guessed, false is returned

    

def play_hangperson(secret):
    """ (str) -> None
    function to coordinate playing a game of hangperson. It calls all the
    functions performing different tasks in the execution of the game
    """
    unique_letters_guessed=""                                   #variable to keep track of letters inputted as a guess
    current_guess_state=initialise_guess_state(secret)          #list to keep track which letters of the word has been guessed already and which yet have to be guessed
    wrong_guesses=0                                             #variable to keep track of the number of wrong guesses
    attempts_exhausted=False                                    #boolean variable to keep track of whether user has used all his tries of wrong inputs(7)
    win=False                                                   #boolean variable to keep track of whether user has won or not
                                  
    while not attempts_exhausted and not win:                   #loop that runs continuously, until the player correctly guesses the secret word or he guesses incorrectly for 7 times
        print_gallows(wrong_guesses)                            #function call to print the gallows
        print(current_guess_state)                              #the current_guess_state printed
        print("Already guessed",unique_letters_guessed)         #function call to print letters that have already been guessed        
        
        guess=new_guess(unique_letters_guessed)                 #function that returns a valid input for guess
        unique_letters_guessed+=guess                           #function calls to update the string unique_letters_guessed
                                                                #which keeps the letters that have already been entered as guess
    

        current_guess_state=update_guess_state(current_guess_state.split(),guess,secret) #function call that updates the current_guess_state
        
        wrong_guesses=update_wrong_attempts(wrong_guesses,guess,secret) #function that updates the number of wrong guesses, if the current guess is wrong
        attempts_exhausted=check_attempts_exhausted(wrong_guesses)      #function that checks if the user has guessed incorrectly for 7 times or if he still has some tries left
        
        win=check_win(current_guess_state,secret)                       #function that checks if the user has guessed the entire word correctly
        
        
        
    if win:                                                             
        print("Congratulations you won the game!")

    if attempts_exhausted:
        print("You didnt win this time :( Better luck next time!! The word was",secret)
        

def evil_hangman(words):
    """ (list) -> list
    function that accepts a list of words and modifies the list by deleting
    elements which have the guess letter in them until every word in
    the letter has the guess letter. The function then returns this list
    """
    not_found=False
    while not(not_found):                   #loop that runs until there isnt any letter left in the list which does not have the guessed letter in it
        not_found=True                      #variable that keeps track whether there is atleast one word which does not have the guessed letter in it
        one_word_without_letter=False
        element=[]
        guess=new_guess("")
        for i in range(len(words)):         #loop that iterates through all the elements of the word list and populates the list elements with elements from word list having the guessed letter in them
            if guess.upper() in words[i]:
                not_found=False
                element.append(words[i])
            else:
                one_word_without_letter=True    #if there is atleast one word in the list which does not have the guessed letter in it, this variable is set to true
        if not(not_found) and one_word_without_letter: #if there is atleast one element in word list which does not have the guessed letter in it, and there are elements in the word list which do have the guessed letter in them, those words are removed from the list
            for i in range(len(element)):               #loop to remove from the word list the words which have the guessed letter in them
                if element[i] in words:
                    words.remove(element[i])
        if not(one_word_without_letter):                #if there isnt any word which does not have the guessed letter in them, the loop is exited
            break
        else:
            print("Your guess is not in the word")
    return words                                        #this list of words is returned



    
def main():
    '''() -> ()

    main function for playing hangperson
    '''
    words = ['APPLE', 'PUMPKIN', 'SCARECROW', 'BAT', 'GHOST','CROQUET','CRYPT','IVORY','COLGATE','JUKEBOX','KIOSK','QUAD','ZIGZAG','ZOMBIE','ALPHA','BETA','GAMMA','RHYTHM','MELODY','GUITAR','PIANO','FORTISSIMO']
    words=choose_version(words)
    secret=choose_secret_word(words)
    play_hangperson(secret)

    
    


main()
