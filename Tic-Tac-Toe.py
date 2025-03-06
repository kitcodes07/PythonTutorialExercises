from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    boarder = "+-------+-------+-------+"
    middle = "|       |       |       |"
    with_num = ["|   ", "   |   ", "   |   ", "   |"]
    for row in range(3):
        print(boarder, middle, sep='\n')
        print(with_num[0], board[row][0], with_num[1], board[row][1], with_num[2], board[row][2], with_num[3], sep='')
        print(middle)
    print(boarder)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    while True:
        move = str(input("Enter your move: "))
        for r in range(3):
            for c in range(3):
                if board[r][c] == move:
                    board[r][c] = 'O'
                    return board
        print("Not valid. Please select a free field.")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    # free_fields = []
    #
    # for row in range(3):
    #     for column in range(3):
    #         if board[row][column] != 'O' and board[row][column] != 'X':
    #             free_fields.append((row, column))
    # shorter list comprehension as the above commented code
    free_fields = [(row, column) for row in range(3) for column in range(3) if
                   board[row][column] != 'O' and board[row][column] != 'X']

    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    # rows
    # for i in range(3):
    #     if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign: return True
    #
    # # columns
    # for i in range(3):
    #     if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign: return True
    #
    # # diagonals
    # if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign: return True
    # if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign: return True

    # diagonals
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign: return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign: return True

    # rows and columns
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign: return True
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign: return True



    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.

    free_fields = make_list_of_free_fields(board)
    move = free_fields[randrange(len(free_fields))]
    board[move[0]][move[1]] = 'X'

    return board


# r_board = [['' for row in range(3)] for column in range(3)]
# value = 1
# for i in range(3):
#     for j in range(3):
#         if value == 5:
#             r_board[i][j] = 'X'
#         else:
#             r_board[i][j] = str(value)
#         value += 1
#shorter list comprehension as the above commented code
r_board = [[str(value) if value != 5 else 'X' for value in range(i * 3 + 1, i * 3 + 4)] for i in range(3)]

display_board(r_board)
while True:
    enter_move(r_board)
    display_board(r_board)
    if victory_for(r_board, 'O'):
        print("You won!")
        break
    draw_move(r_board)
    display_board(r_board)
    if victory_for(r_board, 'X'):
        print("Computer won!")
        break
    if len(make_list_of_free_fields(r_board)) == 0:
        print("It's a tie!")
        break



