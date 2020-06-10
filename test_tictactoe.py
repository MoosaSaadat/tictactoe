import unittest
import tictactoe


class TestTicTacToe(unittest.TestCase):
    def test_player(self):
        board = [
            [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
            [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
            [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
        ]
        result = tictactoe.player(board)
        self.assertEqual(result, tictactoe.X)

        board[0][0] = tictactoe.X
        result = tictactoe.player(board)
        self.assertEqual(result, tictactoe.O)

        board[0][1] = tictactoe.O
        result = tictactoe.player(board)
        self.assertEqual(result, tictactoe.X)

    def test_actions(self):
        board = [
            [tictactoe.X, tictactoe.O, tictactoe.EMPTY],
            [tictactoe.O, tictactoe.O, tictactoe.X],
            [tictactoe.X, tictactoe.EMPTY, tictactoe.EMPTY],
        ]
        result = tictactoe.actions(board)
        self.assertEqual(result, [(0, 2), (2, 1), (2, 2)])

        board[2][2] = tictactoe.X
        result = tictactoe.actions(board)
        self.assertEqual(result, [(0, 2), (2, 1)])

        board[0][2] = tictactoe.O
        result = tictactoe.actions(board)
        self.assertEqual(result, [(2, 1)])


if __name__ == "__main__":
    unittest.main()
