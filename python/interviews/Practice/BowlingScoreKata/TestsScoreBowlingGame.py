from logging import NullHandler
import unittest
from ScoreBowlingGame import ScoreBowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.bowling_game = ScoreBowlingGame()

    def test_GameCreate(self):
         self.assertIsInstance(self.bowling_game, ScoreBowlingGame)

    def test_GameAllZeros(self):
        self.helper_roll_many(0, 20)
        self.assertEquals(self.bowling_game.score(), 0)

    def test_GameAllOnes(self):
        self.helper_roll_many(1, 20)
        self.assertEquals(self.bowling_game.score(), 20)

    def helper_roll_many(self, pins_knocked_down, num_rolls):
        for _ in range(num_rolls):
            self.bowling_game.roll(pins_knocked_down)



if __name__ == "__main__":
    unittest.main()

