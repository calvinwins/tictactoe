#tic tac toe with AI
#Using git hub
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




board = [' ' for x in range(9)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print(f'''
    {board[0]}|{board[1]}|{board[2]}
    -----
    {board[3]}|{board[4]}|{board[5]}
    -----
    {board[6]}|{board[7]}|{board[8]}''')
    print()
def isWinner(val, le):
    return (val[0] == le and val[1] == le and val[2] == le or
            val[3] == le and val[4] == le and val[5] == le or
            val[6] == le and val[7] == le and val[8] == le or
            val[0] == le and val[3] == le and val[6] == le or
            val[1] == le and val[4] == le and val[7] == le or
            val[2] == le and val[5] == le and val[8] == le or
            val[0] == le and val[4] == le and val[8] == le)

def playerMove():
    play = True
    while play:
        move = input('Please select a position to place an \'X\' (0-8): ')
        try:
            move = int(move)
            if move > -1 and move < 9:
                if spaceIsFree(move):
                    play = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [0,2,6,8]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [1,3,5,7]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

if __name__ == "__main__":
    main()