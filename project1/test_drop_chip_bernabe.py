"""
Joseph Bernabe
Oct 26, 2025
Project 2, Part 2
"""

import unittest
from main import Connect4

class TestDropChip(unittest.TestCase):

    def setUp(self):
        self.game = Connect4()

    def test_successful_drop(self):
        result = self.game.drop_chip(1)
        self.assertTrue(result)
        self.assertEqual(self.game.board[5][0], 'X')

    def test_full_column(self):
        for _ in range(self.game.ROWS):
            self.game.drop_chip(1)
            self.game.switch_player()
        result = self.game.drop_chip(1)
        self.assertFalse(result)

    def test_invalid_column_low(self):
        result = self.game.drop_chip(0)
        self.assertFalse(result)

    def test_invalid_column_high(self):
        result = self.game.drop_chip(8)
        self.assertFalse(result)

    def test_full_board(self):
        for col in range(1, self.game.COLS + 1):
            for _ in range(self.game.ROWS):
                self.game.drop_chip(col)
                self.game.switch_player()
        result = self.game.drop_chip(4)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()