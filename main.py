import random
from math import sqrt, pi, cos, sin
from textwrap import fill
from turtle import color
from scipy.stats import ttest_ind, shapiro, levene, mannwhitneyu
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


class Dartboard_1:
    
    def __init__(self):
        self.scores = []
        self.historyOfCoordinates = []
        self.radiusOfBoard = 0.5
    
    def throw(self):
        x = random.uniform(-self.radiusOfBoard,self.radiusOfBoard)
        y = random.uniform(-self.radiusOfBoard,self.radiusOfBoard)
        coordinates = (x,y)
        distanceFrom0 = sqrt(x**2+y**2)
        
        if distanceFrom0 > self.radiusOfBoard:
            score = 0
        elif distanceFrom0 < (self.radiusOfBoard/10):
            score = 5
        elif distanceFrom0 >= (self.radiusOfBoard/10) and distanceFrom0 < (self.radiusOfBoard/5):
            score = 4
        elif distanceFrom0 >= (self.radiusOfBoard/5) and distanceFrom0 < (self.radiusOfBoard/2):
            score = 3  
        elif distanceFrom0 >= (self.radiusOfBoard/2) and distanceFrom0 < (self.radiusOfBoard/1.25):
            score = 2
        else:
            score = 1
            
        self.save_score(coordinates, score)  
    
    def save_score(self, coordinates, score):
        self.historyOfCoordinates.append(coordinates)
        self.scores.append(score)
    
    def simulate(self, nrOfRounds):
        for _ in range(nrOfRounds):
            self.throw()
        
        self.averageScore = sum(self.scores)/nrOfRounds
    
     
    def show_board(self):
        x = [round[0] for round in self.historyOfCoordinates]
        y = [round[1] for round in self.historyOfCoordinates]
        circle1 = Circle((0,0), radius=self.radiusOfBoard/10, color='darkslategrey', alpha=0.4, edgecolor='none')
        circle2 = Circle((0,0), radius=self.radiusOfBoard/5, color='darkcyan', alpha=0.4, edgecolor='none')
        circle3 = Circle((0,0), radius=self.radiusOfBoard/2, color='cadetblue', alpha=0.4, edgecolor='none')
        circle4 = Circle((0,0), radius=self.radiusOfBoard/1.25, color='powderblue', alpha=0.4, edgecolor='none')
        
        fig, ax = plt.subplots(figsize=(5,5)) 
        
        ax.add_patch(circle4)
        ax.add_patch(circle3)
        ax.add_patch(circle2)
        ax.add_patch(circle1)
        plt.scatter(x,y, color='darkslategrey', s=5)
        plt.show()
        
class Dartboard_2:
    
    def __init__(self):
        self.scores = []
        self.historyOfCoordinates = []
        self.radiusOfBoard = 0.5
    
    def throw(self):
        a = self.radiusOfBoard/0.5
        
        r = random.uniform(0,a * 1/sqrt(pi))
        phi = random.uniform(0,2*pi)
        x = r*cos(phi)
        y = r*sin(phi)
        coordinates = (x,y)
        distanceFrom0 = sqrt(x**2+y**2)
        
        if distanceFrom0 > self.radiusOfBoard:
            score = 0
        elif distanceFrom0 < (self.radiusOfBoard/10):
            score = 5
        elif distanceFrom0 >= (self.radiusOfBoard/10) and distanceFrom0 < (self.radiusOfBoard/5):
            score = 4
        elif distanceFrom0 >= (self.radiusOfBoard/5) and distanceFrom0 < (self.radiusOfBoard/2):
            score = 3    
        elif distanceFrom0 >= (self.radiusOfBoard/2) and distanceFrom0 < (self.radiusOfBoard/1.25):
            score = 2
        else:
            score = 1
        self.save_score(coordinates, score)  
    
    def save_score(self, coordinates, score):
        self.historyOfCoordinates.append(coordinates)
        self.scores.append(score)
    
    def simulate(self, nrOfRounds):
        for _ in range(nrOfRounds):
            self.throw()
        
        self.averageScore = sum(self.scores)/nrOfRounds
        
    def show_board(self):
        super().Dartboard_1.show_board()
            


def test_equal_means(firstSample : Dartboard_1, secondSample : Dartboard_2, alpha = 0.05):
    #h0 -> mean of scores from dartboard_1 = mean of scores from dartboard_2
    
    #normality test
    stat1, p1 = shapiro(firstSample.scores)
    stat2, p2 = shapiro(secondSample.scores)
    #test - equal variances
    statLevene, pLevene = levene(firstSample.scores, secondSample.scores)
    
    if p1 > 0.05 and p2 > 0.05 and pLevene > 0.05:
        #t test if variables are normally distributed and their variances are equal
        stat, p = ttest_ind(firstSample.scores, secondSample.scores)
    else:
        #non-parametric test
        stat, p = mannwhitneyu(firstSample.scores, secondSample.scores)
    
    if p > alpha:
        #there is no reason to reject h0
        print(f"There isn't a significant difference between average scores of dartboard 1 and dartboard 2. We don't reject h0 at a significance level of {p}.")
        print(f'Average scores: dartboard 1 = {firstSample.averageScore}, dartboard 2 = {secondSample.averageScore}')
        
    else:
        print(f"There is a significant difference between average scores of dartboard 1 and dartboard 2. We reject h0 at a significance level of {alpha}.")
        print(f'Average scores: dartboard 1 = {firstSample.averageScore}, dartboard 2 = {secondSample.averageScore}')




playFirstDartboard = Dartboard_1()
playFirstDartboard.simulate(200)
playSecondDartboard = Dartboard_2()
playSecondDartboard.simulate(200)
test_equal_means(playFirstDartboard,playSecondDartboard)
playFirstDartboard.show_board()