class Cell:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.nextState = None
    
    def updateState(self):
        self.state = self.nextState
        self.nextState = None