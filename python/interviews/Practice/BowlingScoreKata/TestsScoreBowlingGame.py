import unittest
from ScoreBowlingGame import ScoreBowlingGame

class TestBowlingGame(unittest.TestCase):
    def test_GameCreate(self):
         bowling_game = ScoreBowlingGame()
         self.assertIsInstance(bowling_game, ScoreBowlingGame)

    def test_GameAllZeros(self):
        bowling_game = ScoreBowlingGame()
        for _ in range(20):
            bowling_game.roll(0)
        self.assertEquals(bowling_game.score(), 0)

    def test_GameAllOnes(self):
        bowling_game = ScoreBowlingGame()
        for _ in range(20):
            bowling_game.roll(1)
        self.assertEquals(bowling_game.score(), 20)


if __name__ == "__main__":
    unittest.main()

