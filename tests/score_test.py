import unittest
from src.main import Player

player = Player()
player_expected = Player(100, 1)

class TestScore(unittest.TestCase):
    def test_add(self):
        # Checar si respuesta del usuario (arg1) es igual al codigo actual (arg2) y suma 1 al score
        self.assertEqual(, pla)
