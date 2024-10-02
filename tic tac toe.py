import math
def create_board():
    return [' ' for _ in range(9)]  
def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
def winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]  
    return any(board[i] == board[j] == board[k] == player for i, j, k in win_conditions)
def is_tie(board):
    return ' ' not in board
def minimax(board, depth, alpha, beta, maximizing):
    if winner(board, 'X'):
        return -1  
    if winner(board, 'O'):
        return 1   
    if is_tie(board):
        return 0   
    
    if maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval
def ai_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'
def human_move(board):
    move = int(input("Enter your move (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("Invalid move. Try again.")
        human_move(board)
def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        human_move(board)
        print_board(board)

        if winner(board, 'X'):
            print("You win!")
            break
        if is_tie(board):
            print("It's a tie!")
            break
        ai_move(board)
        print("AI's move:")
        print_board(board)

        if winner(board, 'O'):
            print("AI wins!")
            break
        if is_tie(board):
            print("It's a tie!")
            break
if __name__ == '__main__':
    play_game()
