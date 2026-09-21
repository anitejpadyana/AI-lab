import copy

def main():
    intro()
    board = get_custom_board()
    print_pretty(board)
    symbol_1, symbol_2 = "X", "O"
    
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    count = x_count + o_count + 1
    
    play_game_from_state(board, symbol_1, symbol_2, count)

def intro():
    print("You will input a half-done board. You are X (Human) and the computer is O (Computer).")
    print("For every computer move, the path cost (number of states evaluated) will be printed.\n")

def get_custom_board():
    print("Please input the current half-done board row by row.")
    print("Use 'X', 'O', or space ' ' for empty cells.")
    board = []
    for i in range(3):
        while True:
            row_input = input(f"Enter row {i+1} (3 characters, e.g., 'X O'): ")
            if len(row_input) == 3:
                board.append([char.upper() for char in row_input])
                break
            print("Invalid input! Please enter exactly 3 characters.")
    return board

def print_pretty(board):
    print("\n---+---+---")
    for r in range(3):
        print(f" {board[r][0]} | {board[r][1]} | {board[r][2]} ")
        print("---+---+---")
    print()

def get_empty_cells(board):
    cells = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                cells.append((r, c))
    return cells

def is_winner_state(board, symbol):
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == symbol:
            return True
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == symbol:
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
            return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
            return True
    return False

def minimax(board, depth, is_maximizing, computer_sym, human_sym, state_counter):
    state_counter[0] += 1
    
    if is_winner_state(board, computer_sym):
        return 10 - depth
    if is_winner_state(board, human_sym):
        return depth - 10
    if not get_empty_cells(board):
        return 0
        
    if is_maximizing:
        best_score = -float('inf')
        for r, c in get_empty_cells(board):
            board[r][c] = computer_sym
            score = minimax(board, depth + 1, False, computer_sym, human_sym, state_counter)
            board[r][c] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for r, c in get_empty_cells(board):
            board[r][c] = human_sym
            score = minimax(board, depth + 1, True, computer_sym, human_sym, state_counter)
            board[r][c] = " "
            best_score = min(score, best_score)
        return best_score

def computer_move(board, computer_sym, human_sym):
    best_score = -float('inf')
    best_move = None
    state_counter = [0]
    
    for r, c in get_empty_cells(board):
        board[r][c] = computer_sym
        score = minimax(board, 0, False, computer_sym, human_sym, state_counter)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            best_move = (r, c)
            
    return best_move, state_counter[0]

def play_game_from_state(board, symbol_1, symbol_2, count):
    winner = None
    
    while count <= 9:
        if count % 2 == 1:
            print("--- Player X (Human) Turn ---")
            while True:
                try:
                    row = int(input("Pick a row (0, 1, or 2): "))
                    col = int(input("Pick a col (0, 1, or 2): "))
                    if 0 <= row <= 2 and 0 <= col <= 2:
                        if board[row][col] == " ":
                            board[row][col] = symbol_1
                            break
                        else:
                            print("Square already filled!")
                    else:
                        print("Out of bounds! Choose 0, 1, or 2.")
                except ValueError:
                    print("Please enter valid integers.")
        else:
            print("--- Player O (Computer) Turn ---")
            move, path_cost = computer_move(board, symbol_2, symbol_1)
            if move:
                board[move[0]][move[1]] = symbol_2
                print(f"Computer plays at row {move[0]}, col {move[1]}.")
                print(f"Path cost (states evaluated): {path_cost}")
        
        print_pretty(board)
        
        if is_winner_state(board, symbol_1):
            winner = symbol_1
            break
        if is_winner_state(board, symbol_2):
            winner = symbol_2
            break
            
        count += 1
        
    if winner:
        print(f"Game Over! Winner is Player {winner}.")
    else:
        print("Game Over! It's a draw.")

if __name__ == "__main__":
    main()
