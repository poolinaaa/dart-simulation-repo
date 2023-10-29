import random
from math import sqrt, pi

class Dartboard_1:
    
    def __init__(self):
        self.scores = []
        self.historyOfCoordinates = []
        self.radiusOfBoard = 0.5
    
    def throw(self):
        x = random.uniform(0,self.radiusOfBoard)
        y = random.uniform(0,self.radiusOfBoard)
        coordinates = (x,y)
        distanceFrom0 = sqrt(x**2+y**2)
        
        if distanceFrom0 > self.radiusOfBoard:
            score = 0
        elif distanceFrom0 < (self.radiusOfBoard/10):
            score = 5
        elif distanceFrom0 >= (self.radiusOfBoard/10) and distanceFrom0 < (self.radiusOfBoard/2.5):
            score = 3
        elif distanceFrom0 >= (self.radiusOfBoard/2.5) and distanceFrom0 < (self.radiusOfBoard/1.25):
            score = 2
        else:
            score = 1
        self.save_score(coordinates, score)  
    
    def save_score(self, coordinates, score):
        self.historyOfCoordinates.append(coordinates)
        self.scores.append(score)
    
    def simulate(self, nrOfRounds):
        pass