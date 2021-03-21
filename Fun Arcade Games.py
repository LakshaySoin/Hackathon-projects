from random import randint
import sys

def PickGame():
    while True:
        try:
            decision = str(input("Welcome to Soin's Soothing Gaming Shop! We have two games for you to play, Whack a Yak! and Tic-Tac Toe.\nWhich game would you like to play first (Enter w or t): "))
            decision = decision.lower()
            if decision == 'w':
                WhichGame(condition = True)
            elif decision == 't':
                WhichGame(condition = False)
            else:
                print("Please enter w or t")
        except ValueError:
            print("Enter a letter pls")

def Intro():
    while True:
        try:
            introduction = str(input("Welcome to Whack an Invisible Yak!\nIn this game, you will chose a number from 1-12 and see if you hit an invisible Yak!\nEach hit gives you 30 points, and a special hit gives you 50 points. If you reach 300 points, you win.\nbut if you take to long (number of turns based on difuculty level), you will lose.\nWhat difficulty would you like? (easy, medium, or hard): "))
            global intro
            intro = introduction.lower()
            Pickednumber()
            BonusPoints()
            if intro == 'easy':
                print(Easy())
            elif intro == 'medium':
                print(Medium())
            elif intro == 'hard':
                print(Hard())
            else:
                print("Nuh uh. Enter easy, medium, or hard")
        except ValueError:
            print("You gotta enter a word")

dict = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'11', 12:'12'}

def Board():
    print("----|----|----|----")
    print("| " + dict[1] + " |  " + dict[2] + " |  " + dict[3] + " |  " + dict[4] +" |")
    print("----|----|----|----")
    print("| " + dict[5] + " |  " + dict[6] + " |  " + dict[7] + " |  " + dict[8] +" |")
    print("----|----|----|----")
    print("| " + dict[9] + " | " + dict[10] + " | " + dict[11] + " | " + dict[12] +" |")
    print("----|----|----|----")

def Pickednumber():
    global the_number
    the_number = randint(1, 12)

counter = 0

def BoardChange():
    dict[user_move] = 'X'
    Board()
    dict[user_move] = str(user_move)

def Score(lucky):
    global counter
    if lucky != True:
        counter += 30
    else:
        counter += 50
    score = counter
    if score >= 300:
        print("Your score is " + str(score))
        print("You won in " + str(moves) + " moves!")
        PlayAgain()
    else:
        print("Your score is " + str(score))

def BonusPoints():
    global the_lucky_number
    the_lucky_number = randint(1, 12)

moves = 0

def Easy():
    try:
        while True:
            global moves
            Board()
            global user_move
            user_move = int(input("Enter a number from 1 - 12 (Enter a letter to exit): "))
            if moves == 50:
                print("Dang man, the yak evaded you to many times")
                PlayAgain()
            elif user_move == the_lucky_number:
                BoardChange()
                print("My goodness! You hit a special yak!")
                moves += 1
                Score(lucky = True)
                Pickednumber()
                BonusPoints()
            elif user_move == the_number:
                BoardChange()
                print("Nice you got a hit!")
                moves += 1
                Score(lucky = False)
                Pickednumber()
                BonusPoints()
            else:
                BoardChange()
                print("Rats! The yak was not there")
                moves += 1
                Pickednumber()
                BonusPoints()
    except ValueError:
        print("Goodbye")
        sys.exit()

def Medium():
    try:
        while True:
            global moves
            Board()
            print(user_move)
            if moves == 40:
                print("Dang man, the yak evaded you to many times")
                PlayAgain()
            elif user_move == the_lucky_number:
                BoardChange()
                print("My goodness! You hit a special yak !")
                moves += 1
                Score(lucky = True)
                Pickednumber()
                BonusPoints()
            elif user_move == the_number:
                BoardChange()
                print("Nice you got a hit!")
                moves += 1
                Score(lucky = False)
                Pickednumber()
                BonusPoints()
            else:
                BoardChange()
                print("Rats! The yak was not there")
                moves += 1
                Pickednumber()
                BonusPoints()
    except ValueError:
        print("Goodbye")
        sys.exit()

def Hard():
    try:
        while True:
            global moves
            Board()
            print(user_move)
            if moves == 25:
                print("Dang man, the yak evaded you to many times")
                PlayAgain()
            elif user_move == the_lucky_number:
                BoardChange()
                print("My goodness! You hit a special yak!")
                moves += 1
                Score(lucky = True)
                Pickednumber()
                BonusPoints()
            elif user_move == the_number:
                print("Nice you got a hit!")
                moves += 1
                Score(lucky = False)
                Pickednumber()
                BonusPoints()
            else:
                BoardChange()
                print("Rats! The yak was not there")
                moves += 1
                Pickednumber()
                BonusPoints()
    except ValueError:
        print("Goodbye")
        sys.exit()

def PlayAgain():
    while True:
        try:
            again = str(input("Would you like to play again (y or n or enter anything else to exit): "))
            if again == 'y':
                Reset()
                Intro()
            else:
                print("Goodbye")
                sys.exit()
        except ValueError:
            print("Enter a letter pls")

def Reset():
    global counter
    global moves
    counter = 0
    moves = 0

from random import randrange
import sys

board = {1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6',
        7: '7', 8: '8', 9: '9'}

count = 1

def Introduction():
    while True:
        try:
            global welcome
            welcome = str(input("Welcome to Tic-Tac-Toe! In this game, you will need to pick a number from 1-9.\nThis number will be placed on the board and whoever gets 3 squares in a row, column, or diagonal wins.\nWould you like to play aganist the computer or another player (enter c or p): "))
            welcome = welcome.lower()
            if welcome == 'c' or welcome == 'p':
                DisplayBoard()
                User1Move()
            else:
                print("Please enter c or p")
        except ValueError:
            print("Enter a letter please")

def DisplayBoard():
   print("+-------+-------+-------+")
   print("|       |       |       |")
   print("|      " + board[1] + "|    " + board[2] + "  |  " + board[3] + "    |")
   print("|       |       |       |")
   print("+-------+-------+-------+")
   print("|       |       |       |")
   print("|      " + board[4] + "|    " + board[5] + "  |  " + board[6] + "    |")
   print("|       |       |       |")
   print("+-------+-------+-------+")
   print("|       |       |       |")
   print("|      " + board[7] + "|    " + board[8] + "  |  " + board[9] + "    |")
   print("|       |       |       |")
   print("+-------+-------+-------+")

def User1Move():
    global count
    while True:
        global user1move
        user1move = int(input("Enter your move: "))
        if user1move < 1:
            print("Not acceptable")
        elif user1move > 9:
            print("Not acceptable")
        elif board[user1move] == 'X':
            print("Not acceptable")
        elif board[user1move] == 'O':
            print("You already entered that")
        else:
            board[user1move] = 'O'
            count += 1
            Victory()
            if welcome == 'p':
                DisplayBoard()
                User2Move()
            else:
                DisplayBoard()
                ComputerMove()


def User2Move():
    global count
    while True:
        global user2move
        user2move = int(input("Enter your move: "))
        if user2move < 1:
            print("Not acceptable")
        elif user2move > 9:
            print("Not acceptable")
        elif user2move == 5:
            print("Not acceptable")
        elif board[user2move] == 'O':
            print("Not acceptable")
        elif board[user2move] == 'X':
            print("You already entered that")
        else:
            board[user2move] = 'X'
            count += 1
            Victory()
            DisplayBoard()
            User1Move()

def Victory():
   global count
   if board[3] == board[5] and board[5] == board[7] and board[3] and board[7] and board[3] != '':
       if board[3] == 'O':
           print("User1 has won")
           PlayOnceAgain()
       elif board[3] == 'X' and welcome == 'c':
           print("The computer has won")
           PlayOnceAgain()
       elif board[1] == 'X' and welcome == 'p':
           print("User2 has won")
           PlayOnceAgain()
       else:
           print("Please continue")
   elif board[3] == board[6] and board[6] == board[9] and board[3] == board[9] and board[3] != '':
       if board[3] == 'O':
           print("User1 has won")
           PlayOnceAgain()
       elif board[3] == 'X' and welcome == 'c':
           print("The computer has won")
           PlayOnceAgain()
       elif board[1] == 'X' and welcome == 'p':
           print("User2 has won")
           PlayOnceAgain()
       else:
           print("Please continue")
   elif board[2] == board[5] and board[5] == board[8] and board[2] == board[8] and board[2] != '':
       if board[2] == 'O':
           print("User1 has won")
           PlayOnceAgain()
       elif board[2] == 'X' and welcome == 'c':
           print("The computer has won")
           PlayOnceAgain()
       elif board[1] == 'X' and welcome == 'p':
           print("User2 has won")
           PlayOnceAgain()
       else:
           print("Please continue")
   elif board[7] == board[8] and board[8] == board[9] and board[7] == board[9] and board[7] != '':
       if board[7] == 'O':
           print("User1 has won")
           PlayOnceAgain()
       elif board[7] == 'X' and welcome == 'c':
           print("The computer has won")
           PlayOnceAgain()
       elif board[1] == 'X' and welcome == 'p':
           print("User2 has won")
           PlayOnceAgain()
       else:
           print("Please continue")
   elif board[4] == board[5] and board[5] == board[6] and board[4] == board[6] and board[4] != '':
       if board[4] == 'O':
           print("User1 has won")
           PlayOnceAgain()
       elif board[4] == 'X' and welcome == 'c':
           print("The computer has won")
           PlayOnceAgain()
       elif board[1] == 'X' and welcome == 'p':
           print("User2 has won")
           PlayOnceAgain()
       else:
           print("Please continue")
   elif board[1] == board[5] and board[5] == board[9] and board[1] == board[9] and board[1] != '':
       if board[1] == 'O':
           print("User1 has won")
           PlayOnceAgain()
       elif board[1] == 'X' and welcome == 'c':
           print("The computer has won")
           PlayOnceAgain()
       elif board[1] == 'X' and welcome == 'p':
           print("User2 has won")
           PlayOnceAgain()
       else:
           print("Please continue")
   elif board[1] == board[4] and board[4] == board[7] and board[1] == board[7] and board[1] != '':
       if board[1] == 'O':
           print("User1 has won")
           PlayOnceAgain()
       elif board[1] == 'X' and welcome == 'c':
           print("The computer has won")
           PlayOnceAgain()
       elif board[1] == 'X' and welcome == 'p':
           print("User2 has won")
           PlayOnceAgain()
       else:
           print("Please continue")
   elif board[1] == board[2] and board[2] == board[3] and board[1] == board[3] and board[1] != '':
       if board[1] == 'O':
           print("User1 has won")
           PlayOnceAgain()
       elif board[1] == 'X' and welcome == 'c':
           print("The computer has won")
           PlayOnceAgain()
       elif board[1] == 'X' and welcome == 'p':
           print("User2 has won")
           PlayOnceAgain()
       else:
           print("Please continue")
   elif count == 9:
       print("The game is a tie")
       PlayOnceAgain()
   else:
       print("Please continue")

def ComputerMove():
   global count
   while True:
       for i in range(1):
           computermove = randrange(1,10)
           if computermove == user1move:
               continue
           elif computermove == 5:
               continue
           elif board[computermove] == 'O':
               continue
           elif board[computermove] == 'X':
               continue
           else:
               board[computermove] = 'X'
               count += 1
               Victory()
               DisplayBoard()
               User1Move()

def PlayOnceAgain():
    try:
        again = str(input("Would you like to play again? (y or n): "))
        again = again.lower()
        if again == 'y':
            ResetBoard()
            Introduction()
        else:
            print("See you later")
            sys.exit()
    except ValueError:
        print("Enter a letter please")

def ResetBoard():
    global board
    board = {1: '1', 2: '2', 3: '3',
             4: '4', 5: '5', 6: '6',
             7: '7', 8: '8', 9: '9'}

def WhichGame(condition):
    if condition == True:
        Intro()
    else:
        Introduction()

PickGame()