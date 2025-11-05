import unittest
from src.player import Player

class TestScore(unittest.TestCase):
    def test_right_letter(self):
        player = Player()
        player_expected = Player(100, 1)

        player.check_answer("A", ".-")
        self.assertEqual(player.score, player_expected.score)
    def test_wrong_letter(self):
        player = Player(200, 2)
        player_expected = Player(100, 0)

        player.check_answer("B", ".-")
        self.assertEqual(player.score, player_expected.score)
    def test_number_over_nine(self):
        player = Player(200, 2)
        player_expected = Player(100, 0)

        player.check_answer("10", ".-")
        self.assertEqual(player.score, player_expected.score)
    def test_number_under_zero(self):
        player = Player(200, 2)
        player_expected = Player(100, 0)

        player.check_answer("-14", ".-")
        self.assertEqual(player.score, player_expected.score)
