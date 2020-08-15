import random

hangman_graphics = [
    '''
    +----+
         |
         |
         |
        ====
    ''',
    '''
    +----+
    O    |
         |
         |
        ====
    ''',
    '''
       +----+
       O    |
       |    |
            |
           ====
       ''',
    '''
       +----+
       O    |
      /|    |
            |
           ====
       ''',
    '''
           +----+
           O    |
          /|\   |
                |
               ====
           ''',
    '''
           +----+
           O    |
          /|\   |
          /     |
               ====
           ''',
    '''
       +----+
       O    |
      /|\   |
      / \   |
           ====
       ''',
    '''
          +----+
         [O    |
         /|\   |
         / \   |
              ====
          ''',
    '''
          +----+
         [O]   |
         /|\   |
         / \   |
              ====
          '''
]
#using dictionary to store words
words = {'Animals':''''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split(),
         'Colors' :'''red orange yellow green blue indigo violet white black
      brown'''.split(),
        'Shapes':'''square triangle rectangle circle ellipse rhombus trapezoid
      chevron pentagon hexagon septagon octagon'''.split(),
    'Fruits':'''apple orange lemon lime pear watermelon grape grapefruit cherry
      banana cantaloupe mango strawberry tomato'''.split()
         }

# function to generate secret word
def wordGenerator(words):
    key = random.choice(list(words.keys()))
    index = random.randint(0, len(words[key]) - 1)
    return words[key][index], key

# function to start game
def startGame():
    print("WELCOME TO HANGMAN GAME".center(10, '*'))
    print(hangman_graphics[0])
    print(" What is your name ?")
    playerName = str(input())
    print(playerName + ", would you like to play (Yes or No) ?")
    answer = str(input())
    if answer == 'no' or answer == 'No':
        print("Goodbye!")
        quit()

# function to get and check the letter from user
def letterCheck(guessedLetters):
    while True:
        print("Guess a letter ")
        letter = str(input())
        letter = letter.lower()

        if len(letter) != 1:
            print("Give ONE letter")
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            print(" Please type a LETTER ")
        elif letter in guessedLetters:
            print(" You've already guessed that letter. Try again.")
        else:
            return letter

# function to ask player if he wants to play again
def play_again():
    print("Do you want to play again ? Yes or No.")
    answer = str(input())
    if answer == 'no' or answer == 'No':
        return False
    else:
        return True

# function to display letters and hangman
def display(word, attempts, letter, blanks):
    print(hangman_graphics[attempts], end=" ")
    print(" Missed letters : ", end='')

    for el in range(len(word)):
        if word[el] == letter:
            blanks[el] = letter

    for i in range(len(word)):
        print(blanks[i], end=" ")

#function to decide difficulty level
def difficulty():
    difficulty = "X"
    while difficulty not in ['E', 'M', 'H']:
        print(" Enter difficulty : E = Easy , M = Medium, H = Hard")
        difficulty = input().upper()

    if difficulty == "M":
        del hangman_graphics[8]
        del hangman_graphics[7]
    elif difficulty == "H":
        del hangman_graphics[8]
        del hangman_graphics[7]
        del hangman_graphics[5]
        del hangman_graphics[3]

# function to play the game
def play():
    attempt = 0
    gameDone = False
    guessedLetters = list()
    blanks = list()

    startGame()
    difficulty()
    secretWord, wordGroup = wordGenerator(words)
    print(" WORD GROUP is  = ", wordGroup)

    for i in range(len(secretWord)):
        blanks.append('_')
    #print("SECRET = ", secretWord)

    while not gameDone:
        letter = letterCheck(guessedLetters)
        guessedLetters.append(letter)  # save guessed letters in a list
        display(secretWord, attempt, letter, blanks)

        if letter not in secretWord:
            attempt += 1 # add failed attempt

        word = list(secretWord)
        if blanks == word:
            print()
            print(" You won the game !")
            gameDone = True

        elif attempt == len(hangman_graphics):
            print()
            print(" You lost the game !", end=" ")
            print(" The secret word was : " + secretWord)
            gameDone = True

    # ask user to play again
    playAnswer = play_again()
    while playAnswer:
        play()
    print(" Goodbye!")
    quit()

# execution
play()

