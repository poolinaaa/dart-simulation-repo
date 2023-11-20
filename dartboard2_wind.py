import random
from math import sqrt, pi, cos, sin
import matplotlib.pyplot as plt
from main import Dartboard_1
import numpy as np
from scipy.stats import shapiro


class Dartboard_2(Dartboard_1):
    '''class representing the second dartboard, placement of throw is calculated based on drawn radius and angle '''

    name = 'Dartboard 2'

    def __init__(self):
        super().__init__()

    # simulate throw on the second dartboard, placement is calculated based on drawn radius and angle
    def throw(self):
        a = self.radiusOfBoard/0.5

        r = random.uniform(0, a * 1/sqrt(pi))
        phi = random.uniform(0, 2*pi)
        # Random wind effect (from standard normal distribution), it changes x position
        deltaX = self.wind()
        x = r*cos(phi) + deltaX
        y = r*sin(phi)
        coordinates = (x, y)
        distanceFrom0 = sqrt(x**2+y**2)

        # assigning points based on the distance from the center of the dartboard
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

    # bar plot showing amount of every score
    def show_bar_plot(self):
        self.summarize_scores()
        scores_labels = ['0','1','2','3','4','5']
        scores = [self.scoresCount[score] for score in self.scoresCount]
        plt.figure(figsize=(10,6))
        plt.bar(scores_labels,scores,color = 'cadetblue', alpha=0.8)
        plt.title('Amount of a given score')
        plt.xlabel('Points')
        plt.ylabel('Amount of score')
        plt.show()
        
    # test if the scores follow a normal distribution (Shapiro-Wilk test)   
    def test_if_normal(self, alpha = 0.05):
        stat, p = shapiro(self.scores)
        
        #h0 -> scores are normally distributed
        if p > alpha:
            print(f"We don't reject h0 at a significance level of {alpha}.  We have sufficient evidence to say that the scores from {self.name} are normally distributed (p-value: {p})")
        else:
            print(f"Since the p-value is less than {alpha}, we reject h0. We have sufficient evidence to say that the scores from {self.name} are not normally distributed (p-value: {p})")
    
    # simulate wind effect using a normal distribution 
    @staticmethod
    def wind():
        np.random.seed(16)
        rng = np.random.default_rng()
        normalDistrNumber = rng.normal()
        return normalDistrNumber


g = Dartboard_2()
g.simulate(1000)
g.show_board()
g.test_if_normal()
g.show_bar_plot()