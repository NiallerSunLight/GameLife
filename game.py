import random
import time
from cell import Cell

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.initializeGrid()
    
    def initializeGrid(self):
        for y in range(self.height):
            for x in range(self.width):
                state = random.choice([0, 1])
                self.grid[y][x] = Cell(x, y, state)
    
    def getCellNeighbors(self, cell):
        neighbors = []
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue
                nx = cell.x + dx
                ny = cell.y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    neighbor = self.grid[ny][nx]
                    neighbors.append(neighbor)
        return neighbors
    
    def getAliveNeighborCount(self, cell):
        aliveCount = 0
        neighbors = self.getCellNeighbors(cell)
        for neighbor in neighbors:
            if neighbor.state == 1:
                aliveCount += 1
        return aliveCount
    
    def updateGrid(self):
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                aliveNeighbors = self.getAliveNeighborCount(cell)
                
                if cell.state == 1:
                    if aliveNeighbors <= 1 or aliveNeighbors >= 4:
                        cell.nextState = 0
                    else:
                        cell.nextState = 1
                else:
                    if aliveNeighbors == 3:
                        cell.nextState = 1
                    else:
                        cell.nextState = 0
        
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                cell.updateState()
    
    def displayGrid(self):
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                if cell.state == 1:
                    print("■", end=" ")
                else:
                    print("□", end=" ")
            print()
    
    def run(self, numGenerations):
        for generation in range(numGenerations):
            print("Generation:", generation)
            self.displayGrid()
            self.updateGrid()
            time.sleep(1)
