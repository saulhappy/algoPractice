class ScoreBowlingGame():
    def __init__(self):
        self.rolls = []
    
    def roll(self, pins_knocked):
        self.rolls.append(pins_knocked)
    
    def score(self):
        result = 0
        roll_index = 0
        for frame_index in range(10):
            if self.is_spare_frame(roll_index):
                result += self.return_spare_score(roll_index)
            else:
                result += self.return_frame_score(roll_index)
            roll_index += 2
        return result

    def is_spare_frame(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10
    
    def return_spare_score(self, roll_index):
        return 10 + self.rolls[roll_index + 2]

    def return_frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]

