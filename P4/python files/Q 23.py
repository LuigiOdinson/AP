# 23
def check_winner(board):
    won = False
    # ROWS
    for rows in board:
        """duplicates are not allowed in sets so if its length
        is one it means the game's been won"""
        if len(set(rows)) == 1:
            won = True
            return rows[0]
    # COLUMNS
    for i in range(3):
        columns = [board[j][i] for j in range(3)]
        if len(set(columns)) == 1:
            won = True
            return columns[0]
    # DIAGONALS
    for i in range(3):
        for j in range(3):
            if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[0][2]:
                return board[1][1]
    if not won:
        return " "


tic_tac_toe = [["O", "X", "O"],
               ["X", "O", "X"],
               ["O", "X", "O"]]
print(check_winner(tic_tac_toe))
