class ScoreBowlingGame():
    def __init__(self):
        self.rolls = []
    
    def roll(self, pins_knocked):
        self.rolls.append(pins_knocked)
    
    def score(self):
        result = 0
        roll_index = 0
        for frame_index in range(10):
            if self.rolls[roll_index] + self.rolls[roll_index + 1] == 10:
                result += self.rolls[roll_index] + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
            else:
                result += self.rolls[roll_index] + self.rolls[roll_index + 1]
            roll_index += 2
        return result



        # return sum(self.rolls)
