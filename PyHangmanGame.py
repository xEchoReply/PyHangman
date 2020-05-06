import random

def pickWord():
    #Pick random word from SOWPODS dictionary file.
    myList=[]
    with open('sowpods.txt','r') as importList:
        i=importList.readlines()
    return (i[random.randint(0,(len(i)-1))])

def printGameBoard(i):
    #Prints gameboard with space between each letter
    x=""
    for y in i:
        x+=y+" "
    return x

def hangManPics(i):
    #Prints ASCII art, reflecting number of body parts based on wrong guesses.
    pic='''
      +---+
      |   |
      1   |
     324  |
     5 6  |
          |
    ========='''
    if i>=1:
        pic=pic.replace("1","O")
    if i>=2:
        pic=pic.replace("2","|")
    if i>=3:
        pic=pic.replace("3","/")
    if i>=4:
        pic=pic.replace("4","\\")
    if i>=5:
        pic=pic.replace("5","/")
    if i>=6:
        pic=pic.replace("6","\\")
    if i>=0:
        pic=pic.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ")
    return pic

def playHangman():
    #Set initial variables for the game
    correctWord=(str(pickWord()))[:-1].upper()
    wrongGuesses=0
    guesses=set()
    #gameBoard is number of characters in correctWord as underscores until they
    #are guessed.
    gameBoard=[]
    for i in correctWord:
        gameBoard+="_"

    #Start the round by printing ASCII art and current state of the wrod
    while (wrongGuesses<6):
        print("\n"+hangManPics(wrongGuesses))
        print(printGameBoard(gameBoard)+"\n")

        #Prompt for a letter and test if valid or previously guessed
        #If user types in more than one letter, only first letter is tested
        #and counted as their guess
        validAnswer=0
        while validAnswer==0:
            myGuess=str(input("Guess a letter: ")).upper()
            if myGuess[0] in guesses:
                print("You've already guessed that, please try again!\n")
            elif not myGuess[0].isalpha():
                print("Please enter a valid letter!\n")
            else:
                validAnswer=1

        #Test if letter is correct or wrong
        if myGuess[0] in correctWord:
            print("Correct! There is a "+myGuess[0])
            c=0
            while c<len(correctWord):
                if correctWord[c]==myGuess[0]:
                    gameBoard[c]=myGuess[0]
                c+=1
            if not "_" in gameBoard:
                break
        else:
            print("Sorry! There is no "+myGuess[0])
            wrongGuesses+=1

        #Add guess to previous guess list
        guesses.add(myGuess[0])

    #Let player know if they've lost or won the game
    if wrongGuesses>=6:
        print(hangManPics(wrongGuesses))
        print("\nSorry! You lost the game!\nThe word was "+correctWord)
    else:
        print("\nCongratulations! You won!\nThe word was "+correctWord)

if __name__=="__main__":
    playHangman()
