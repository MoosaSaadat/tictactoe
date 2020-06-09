"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Find total number of X in board
    totalX = sum([row.count(X) for row in board])

    # Find total number of O in board
    totalO = sum([row.count(O) for row in board])

    if totalX > totalO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return [
        (i, j)
        for j in range(len(board))
        for i in range(len(board))
        if board[i][j] == EMPTY
    ]


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    actionX, actionY = action

    # Invalid action
    if actionX < 0 or actionX > 2 or actionY < 0 or actionY > 2:
        raise ValueError

    # Make a deep copy
    newBoard = board.copy()

    # Add player sign
    newBoard[actionX][actionY] = player(newBoard)

    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check Rows
    for row in board:
        res = set(row)
        # Winner found
        if len(res) == 1:
            return res.pop()

    # Check Columns
    for col in range(len(board)):
        res = {board[0][col], board[1][col], board[2][col]}
        # Winner found
        if len(res) == 1:
            return res.pop()

    # Check both diagonals
    mainDiagonal = {board[0][0], board[1][1], board[2][2]}
    if len(mainDiagonal) == 1:
        return mainDiagonal.pop()
    antiDiagonal = {board[2][0], board[1][1], board[0][2]}
    if len(antiDiagonal) == 1:
        return antiDiagonal.pop()

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Winner Found
    if winner(board):
        return True

    emptyPositions = [
        EMPTY
        for j in range(len(board))
        for i in range(len(board))
        if board[i][j] == EMPTY
    ]
    # In progress
    if len(emptyPositions):
        return False

    # Tie
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    hasWinner = winner(board)
    if hasWinner == X:
        return 1
    elif hasWinner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
