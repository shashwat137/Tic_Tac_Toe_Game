def display_board(board, player1):
    '''
    Display the board lines for game to play. Board arguement given as a list which basically contains an order of
    positional placements. Even and odd positions will give Xs or Os
    '''
    space = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    if player1 == 'X':
        a = ['X','O']
    else :
        a = ['O','X']
    i = 0
    while i < len(board):
        if i % 2 == 0 :
            space[board[i] - 1] = a[0]
        else :
            space[board[i] - 1] = a[1]
        i += 1


    print('     |     |     ')
    print('  {0}  |  {1}  |  {2}  '.format(space[6],space[7],space[8]))
    print('_____|_____|_____')
    print('     |     |     ')
    print('  {0}  |  {1}  |  {2}  '.format(space[3],space[4],space[5]))
    print('_____|_____|_____')
    print('     |     |     ')
    print('  {0}  |  {1}  |  {2}  '.format(space[0],space[1],space[2]))
    print('     |     |     ')

    return

def game_win(board):
    '''
    Check whether game has ended or not. True if end; False if not
    '''
    i = 0
    p1 = list()
    p2 = list()
    while i < len(board):
        if i % 2 == 0:
            p1.append(board[i])
        else :
            p2.append(board[i])
        i += 1
    if (7 in p1 and 8 in p1 and 9 in p1) or (4 in p1 and 5 in p1 and 6 in p1) or (1 in p1 and 2 in p1 and 3 in p1) or (7 in p1 and 4 in p1 and 1 in p1) or (8 in p1 and 5 in p1 and 2 in p1) or (9 in p1 and 6 in p1 and 3 in p1) or (7  in  p1 and 5 in p1 and 3 in p1) or (9 in p1 and 5 in p1 and 1 in p1):
        return True
    elif (7 in p2 and 8 in p2 and 9 in p2) or (4 in p2 and 5 in p2 and 6 in p2) or (1 in p2 and 2 in p2 and 3 in p2) or (7 in p2 and 4 in p2 and 1 in p2) or (8 in p2 and 5 in p2 and 2 in p2) or (9 in p2 and 6 in p2 and 3 in p2) or (7  in  p2 and 5 in p2 and 3 in p2) or (9 in p2 and 5 in p2 and 1 in p2):
        return True
    else :
        return False

print('Welcome to Tic Tac Toe')
print('There will be two players. Please select whether Player 1 is "X" or "O" ')
while True :
    player1 = input("Enter X or O for Player 1\n")
    player1 = player1.upper()
    if player1 == 'X' or player1 == 'Y':
        break
    else:
        print('Invalid Input\n')
        continue
board =list()


while not game_win(board):
    print('\n'*6)
    if len(board) == 9:
        break
    while True:
        try:
            position = int(input("Enter position for placing your attempt on board using numpad on your keyboard\n"))
            break
        except:
            print("Invalid Input\n")
            continue
    if position in [1,2,3,4,5,6,7,8,9] and position not in board:
        board.append(position)
        display_board(board,player1)
    else:
        print('Invalid Input Please Try again')
        continue



print('\n'*5)
display_board(board,player1)
if game_win(board):
    if len(board) % 2 == 0:
        x = '2'
    else:
        x = '1'
    print('Player{0} has won!!!!'.format(x))    #select which player has one
else:
    print("It is a Draw!!!!")
