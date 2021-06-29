from logging import NullHandler
import unittest
from ScoreBowlingGame import ScoreBowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.bowling_game = ScoreBowlingGame() # Q: why doesn't this accumulate scores?

    def test_GameCreate(self):
         self.assertIsInstance(self.bowling_game, ScoreBowlingGame)

    def test_GameAllZeros(self):
        self.helper_roll_many(0, 20)
        self.assertEquals(self.bowling_game.score(), 0)

    def test_GameAllOnes(self):
        self.helper_roll_many(1, 20)
        self.assertEquals(self.bowling_game.score(), 20)

    def test_GameOneSpareThen6ThenZeros(self):
        self.bowling_game.roll(7)
        self.bowling_game.roll(3)
        self.bowling_game.roll(6)
        self.helper_roll_many(0, 17)
        self.assertEquals(self.bowling_game.score(), 22)

    def helper_roll_many(self, pins_knocked_down, num_rolls):
        for _ in range(num_rolls):
            self.bowling_game.roll(pins_knocked_down)



if __name__ == "__main__":
    unittest.main()

