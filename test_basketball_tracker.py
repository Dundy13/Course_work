import unittest
from unittest.mock import patch
import sqlite3
import os

from basketball_tracker import Player, create_table, track_performance, delete_player

# Assuming the file is named basketball_tracker.py


class TestBasketballTracker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect('test_basketball_performance.db')
        cls.cursor = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        os.remove('test_basketball_performance.db')

    def setUp(self):
        create_table()

    def test_player_initialization(self):
        player = Player("TestPlayer")
        self.assertEqual(player.name, "TestPlayer")
        self.assertEqual(player.points, 0)
        self.assertEqual(player.rebounds, 0)
        self.assertEqual(player.assists, 0)
        self.assertEqual(player.blocks, 0)
        self.assertEqual(player.steals, 0)
        self.assertEqual(player.turnovers, 0)
        self.assertEqual(player.three_pointers_made, 0)
        self.assertEqual(player.two_pointers_made, 0)
        self.assertEqual(player.free_throws_made, 0)

    @patch('builtins.input', side_effect=[10, 5, 3, 2, 1, 4, 2, 1, 3])
    def test_track_performance(self, mock_input):
        player = Player("TestPlayer")
        track_performance(player)
        self.assertEqual(player.points, 10)
        self.assertEqual(player.rebounds, 5)
        self.assertEqual(player.assists, 3)
        self.assertEqual(player.blocks, 2)
        self.assertEqual(player.steals, 1)
        self.assertEqual(player.turnovers, 4)
        self.assertEqual(player.three_pointers_made, 2)
        self.assertEqual(player.two_pointers_made, 1)
        self.assertEqual(player.free_throws_made, 3)

    @patch('builtins.input', return_value=1)
    def test_delete_player(self, mock_input):
        player1 = Player("Player1")
        player2 = Player("Player2")
        players = [player1, player2]
        delete_player(players)
        self.assertEqual(len(players), 1)
        self.assertEqual(players[0].name, "Player2")


if __name__ == '__main__':
    unittest.main()