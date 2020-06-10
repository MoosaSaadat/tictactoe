import unittest
import tictactoe


class TestTicTacToe(unittest.TestCase):
    def test_player(self):
        board = [
            [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
            [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
            [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
        ]

        # Check first player
        result = tictactoe.player(board)
        self.assertEqual(result, tictactoe.X)

        # Check second player
        board[0][0] = tictactoe.X
        result = tictactoe.player(board)
        self.assertEqual(result, tictactoe.O)

        # Check third player
        board[0][1] = tictactoe.O
        result = tictactoe.player(board)
        self.assertEqual(result, tictactoe.X)

    def test_actions(self):
        board = [
            [tictactoe.X, tictactoe.O, tictactoe.EMPTY],
            [tictactoe.O, tictactoe.O, tictactoe.X],
            [tictactoe.X, tictactoe.EMPTY, tictactoe.EMPTY],
        ]

        # Check three actions
        result = tictactoe.actions(board)
        self.assertEqual(result, [(0, 2), (2, 1), (2, 2)])

        # Check two actions
        board[2][2] = tictactoe.X
        result = tictactoe.actions(board)
        self.assertEqual(result, [(0, 2), (2, 1)])

        # Check one actions
        board[0][2] = tictactoe.O
        result = tictactoe.actions(board)
        self.assertEqual(result, [(2, 1)])

    def test_result(self):
        board = [
            [tictactoe.X, tictactoe.O, tictactoe.EMPTY],
            [tictactoe.O, tictactoe.O, tictactoe.X],
            [tictactoe.X, tictactoe.EMPTY, tictactoe.EMPTY],
        ]

        # Check first move
        result = tictactoe.result(board, (0, 2))
        self.assertEqual(
            result,
            [
                [tictactoe.X, tictactoe.O, tictactoe.X],
                [tictactoe.O, tictactoe.O, tictactoe.X],
                [tictactoe.X, tictactoe.EMPTY, tictactoe.EMPTY],
            ],
        )

        # Check second move
        board[0][2] = tictactoe.X
        result = tictactoe.result(board, (2, 1))
        self.assertEqual(
            result,
            [
                [tictactoe.X, tictactoe.O, tictactoe.X],
                [tictactoe.O, tictactoe.O, tictactoe.X],
                [tictactoe.X, tictactoe.O, tictactoe.EMPTY],
            ],
        )

        # Check third move
        board[2][1] = tictactoe.O
        result = tictactoe.result(board, (2, 2))
        self.assertEqual(
            result,
            [
                [tictactoe.X, tictactoe.O, tictactoe.X],
                [tictactoe.O, tictactoe.O, tictactoe.X],
                [tictactoe.X, tictactoe.O, tictactoe.X],
            ],
        )

    def test_winner(self):
        # Check no winner
        board = [
            [tictactoe.X, tictactoe.O, tictactoe.EMPTY],
            [tictactoe.O, tictactoe.O, tictactoe.X],
            [tictactoe.X, tictactoe.X, tictactoe.EMPTY],
        ]
        result = tictactoe.winner(board)
        self.assertIsNone(result)

        # Check vertical match
        board = [
            [tictactoe.X, tictactoe.O, tictactoe.EMPTY],
            [tictactoe.O, tictactoe.O, tictactoe.X],
            [tictactoe.X, tictactoe.O, tictactoe.X],
        ]
        result = tictactoe.winner(board)
        self.assertEqual(result, tictactoe.O)

        # Check horizontal match
        board = [
            [tictactoe.X, tictactoe.O, tictactoe.O],
            [tictactoe.O, tictactoe.O, tictactoe.X],
            [tictactoe.X, tictactoe.X, tictactoe.X],
        ]
        result = tictactoe.winner(board)
        self.assertEqual(result, tictactoe.X)

        # Check main diagonal match
        board = [
            [tictactoe.X, tictactoe.O, tictactoe.O],
            [tictactoe.X, tictactoe.X, tictactoe.EMPTY],
            [tictactoe.O, tictactoe.EMPTY, tictactoe.X],
        ]
        result = tictactoe.winner(board)
        self.assertEqual(result, tictactoe.X)

        # Check anti diagonal match
        board = [
            [tictactoe.X, tictactoe.O, tictactoe.O],
            [tictactoe.X, tictactoe.O, tictactoe.EMPTY],
            [tictactoe.O, tictactoe.X, tictactoe.X],
        ]
        result = tictactoe.winner(board)
        self.assertEqual(result, tictactoe.O)

    def test_terminal(self):
        # Game not finished
        board = [
            [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
            [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
            [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
        ]
        self.assertFalse(tictactoe.terminal(board))

        # Game has a winner
        board = [
            [tictactoe.X, tictactoe.EMPTY, tictactoe.EMPTY],
            [tictactoe.O, tictactoe.X, tictactoe.O],
            [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.X],
        ]
        self.assertTrue(tictactoe.terminal(board))

        # Game is a tie
        board = [
            [tictactoe.X, tictactoe.O, tictactoe.O],
            [tictactoe.O, tictactoe.X, tictactoe.X],
            [tictactoe.X, tictactoe.X, tictactoe.O],
        ]
        self.assertTrue(tictactoe.terminal(board))

    def test_utility(self):
        # Game is a tie
        board = [
            [tictactoe.X, tictactoe.O, tictactoe.O],
            [tictactoe.O, tictactoe.X, tictactoe.X],
            [tictactoe.X, tictactoe.X, tictactoe.O],
        ]
        self.assertEqual(tictactoe.utility(board), 0)

        # X has won
        board = [
            [tictactoe.X, tictactoe.EMPTY, tictactoe.EMPTY],
            [tictactoe.O, tictactoe.X, tictactoe.O],
            [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.X],
        ]
        self.assertEqual(tictactoe.utility(board), 1)

        # O has won
        board = [
            [tictactoe.X, tictactoe.EMPTY, tictactoe.EMPTY],
            [tictactoe.O, tictactoe.O, tictactoe.O],
            [tictactoe.X, tictactoe.EMPTY, tictactoe.X],
        ]
        self.assertEqual(tictactoe.utility(board), -1)


if __name__ == "__main__":
    unittest.main()
