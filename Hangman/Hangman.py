from random import randint

def pick_word(choice):
    """Returns a word from the list along with a censored version of it"""
    val = randint(0, len(choice) - 1)
    word = choice[val].split()
    key = word[:]
    for i in range(len(key)):
        key[i] = ' '.join(key[i])
    answer = " / ".join(key)
    
    for i in range(len(word)):
        hyphen = word[i].find('-')
        if (hyphen >= 0):
            unhyphen = word[i].split('-')
            for j in range(len(unhyphen)):
                unhyphen[j] = ' '.join(len(unhyphen[j]) * '_')
            word[i] = ' - '.join(unhyphen)
        else:
            word[i] = ' '.join(len(word[i]) * '_')
    censored = " / ".join(word)

    return answer, censored


def guessed(guess, guesses):
    '''Checks if the letter entered by the user was already entered this round'''
    for i in guesses:
        if i == guess:
            return True
    else:
        return False


def in_range(letter):
    '''Checks if the entered letter is an acceptable guess, returns False for special characters and multiple characters'''
    total = 0
    for i in range(len(letter)):
        total += ord(letter[i])
    if 65 <= total <= 90:
        return True
    else:
        return False


def check_guess(answer, display, letter):
    '''Checks the guessed letter against the answer, returns true and shows letters in display if correct'''
    match = False
    for i in range(len(answer)):
        if answer[i] == letter:
            display = display[:i] + letter + display[(i+1):]
            match = True
    return display, match


words = ["HELLO WORLD", "MIX-UP", "PYTHON", "STUDENT", "BREAKFAST", 
         "LUNCH", "DINNER", "GOOD MORNING", "PAST-TIME", "RED-HOT",
         "LIGHTNING-FAST", "ICE-COLD", "RAZOR-SHARP", "PITCH-BLACK", 
         "CODING", "LINE-BY-LINE", "HARDWARE", "SOFTWARE", "SPEAKERS",
         "WELCOME HOME", "JAZZ HANDS", "ENERGY DRINK", "TELEVISION",
         "STRINGS", "INTEGERS", "STACKS", "QUEUES", "SCHOLARSHIP",
         "CLASSES", "OBJECTS", "VIDEO GAME"]
wins = 0
losses = 0
playing = True

print("Time for some hangman!")
while (playing):
    answer, display = pick_word(words)
    print("Here's what you have to solve:")
    print(display)
    
    guesses = list()
    wrong = list()
    counter = 0
    win = False
   
    while ((counter < 7) and not win):
        guess = input("\nGuess a letter: ").upper()
        if guessed(guess, guesses):
            print('This letter was already guessed.')
            continue
        if not in_range(guess):
            print('Not an acceptable guess.')
            continue
        guesses.append(guess)
        display, correct = check_guess(answer, display, guess)
        if (correct):
            print(guess, 'was correct.')
            if display.find('_') == -1:
                print(display)
                print('You solved the word! You win!')
                win = True
                wins += 1
                break
        else:
            print(guess, 'was incorrect.')
            counter += 1
            if counter == 7:
                print("That was your 7th incorrect guess, you lose.")
                print("The answer was", answer)
                losses += 1
                break
            wrong.append(guess)
            print('Incorrect guesses so far are', wrong)
        print ("Puzzle so far is", display)
    if (win):
        print("\nCongrats, you beat the computer")
    else:
        print("\nSorry, looks like the computer beat you this time")
    
    print("You have won %d time(s) and the computer has won %d time(s)" % (wins,losses))
    rematch = input("Would you like to play again? (Y/N)").upper()
    while (playing):
        if rematch == 'Y':
            print("\nTime for a new game!")
            break
        elif rematch == 'N':
            print("Thanks for playing!")
            playing = False
        else:
            print("No valid input entered")
            rematch = input("Enter Y or N:").upper()
