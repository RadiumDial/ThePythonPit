import random
import time

# This program combines synthesizes skills learned in Chapter 1-6.
print('Greetings, weary travelor. You must be the one I have been waiting for.')
print('What is your name?')
myName = input()
print('Ah, you are the One. You have one final choice that awaits you, ' + myName)

def displayIntro():
    print('You see these two doors before you?')
    print('One of them will lead you to a place of peace and rest...')
    time.sleep(2)
    print('the other will force you to match wits with a devilish')
    print('scoundrel.')
    print()   

def chooseDoor():
    door = ''
    while door != '1' and door != '2':
        print('Which door will you open? (1 or 2)')
        door = input()

    return door

def checkDoor(chosenDoor):
    print('The door opens as if by an unseen hand...')
    time.sleep(2)
    print('the scent of smoke rekindles a long forgotten memory...')
    time.sleep(2)
    print('a haggard old man peers around the corner and...')
    print()
    time.sleep(2)

    friendlyDoor = random.randint(1,2)

    if chosenDoor == str(friendlyDoor):
        print('gestures to a comfortable easy chair in front of a fine stereo.  You may relax now.')
    else:
        print('challenges you to a guessing game!')

        guessesTaken = 0

        number = random.randint(1, 20)
        print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

        while guessesTaken < 6:
                print('Take a guess.') 
                guess = input()
                guess = int(guess)

                guessesTaken = guessesTaken + 1

                if guess < number:
                    print('Your guess is too low, Moron.') 

                if guess > number:
                    print('Your guess is too high. You stink.')

                if guess == number:
                    break

        if guess == number:
            guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

        if guess != number:
            number = str(number)
        print('Nope. The number I was thinking of was ' , number)  
       
  
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    
    displayIntro()

    doorNumber = chooseDoor()

    checkDoor(doorNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
