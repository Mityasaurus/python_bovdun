from random import randrange


def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")



def enter_move(board):
    free_fields = make_list_of_free_fields(board)
    valid_move = False

    while not valid_move:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            if (move - 1) not in [cell[0] * 3 + cell[1] for cell in free_fields]:
                print("This square is already taken. Try a different move.")
                continue

            valid_move = True
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    row = (move - 1) // 3
    col = (move - 1) % 3
    board[row][col] = 'O'


def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))
    return free_fields


def victory_for(board, sign):
    for row in range(3):
        if all([cell == sign for cell in board[row]]):
            return True
    for col in range(3):
        if all([board[row][col] == sign for row in range(3)]):
            return True
    if all([board[i][i] == sign for i in range(3)]) or all([board[i][2 - i] == sign for i in range(3)]):
        return True
    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    move = randrange(len(free_fields))
    row, col = free_fields[move]
    board[row][col] = 'X'


def play_game():
    board = [[str(i + 1 + j * 3) for i in range(3)] for j in range(3)]
    board[1][1] = 'X'
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("You win!")
            break
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("Computer wins!")
            break
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break


play_game()