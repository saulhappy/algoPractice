class ScoreBowlingGame():
    def __init__(self):
        self.rolls = []
    
    def roll(self, pins_knocked):
        self.rolls.append(pins_knocked)
    
    def score(self):
        return sum(self.rolls)
