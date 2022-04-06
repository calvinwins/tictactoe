#tic tac toe with AI
#Using git hub
#main function to start Tic tac toe program
def main():
    print('Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('The machine beat you!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print('You beat the computer! Good Job!')
            break
        print("Good game. Thanks for playing!") 

    if isBoardFull(board):
        print('Tie Game!')



#list of spaces on board
board = [' ' for x in range(9)]
#function to place position on the board
def insertLetter(letter, pos):
    board[pos] = letter
#funtion of free spaces on board
def spaceIsFree(pos):
    return board[pos] == ' '
#function to print board on the screen
def printBoard(board):
    print(f'''
    {board[0]}|{board[1]}|{board[2]}
    -----
    {board[3]}|{board[4]}|{board[5]}
    -----
    {board[6]}|{board[7]}|{board[8]}''')
    print()
#function to determine if a player is a winner
def isWinner(val, le):
    return (val[0] == le and val[1] == le and val[2] == le or
            val[3] == le and val[4] == le and val[5] == le or
            val[6] == le and val[7] == le and val[8] == le or
            val[0] == le and val[3] == le and val[6] == le or
            val[1] == le and val[4] == le and val[7] == le or
            val[2] == le and val[5] == le and val[8] == le or
            val[0] == le and val[4] == le and val[8] == le or
            val[2] == le and val[4] == le and val[6] == le)
# function of the human players move choice
def playerMove():
    play = True
    while play:
        move = input('Please choose a position to place an \'X\' (0-8): ')
        try:
            move = int(move)
            if move > -1 and move < 9:
                if spaceIsFree(move):
                    play = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is full!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            
#function for the computer moves choice
def compMove():
    possMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    #function of possible conners open
    cornOpen = []
    for i in possMoves:
        if i in [0,2,6,8]:
            cornOpen.append(i)
    #function to choose a random corner that is open        
    if len(cornOpen) > 0:
        move = chooseRandom(cornOpen)
        return move
    #function of total possible moves for the computer
    if 5 in possMoves:
        move = 5
        return move
    #function of possible edge choices
    edgeOpen = []
    for i in possMoves:
        if i in [1,3,5,7]:
            edgeOpen.append(i)
    #function to select a random edge position that is open        
    if len(edgeOpen) > 0:
        move = chooseRandom(edgeOpen)
    
    return move
# a function to make a random choice in a list
def chooseRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    
# a function that determines whether a board is full
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
#a call to the main function
if __name__ == "__main__":
    main()