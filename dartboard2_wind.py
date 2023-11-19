import random
from math import sqrt, pi, cos, sin
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
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

    @staticmethod
    def wind():
        rng = np.random.default_rng()
        normalDistrNumber = rng.normal()
        return normalDistrNumber


g = Dartboard_2()
g.simulate(200)
g.show_board()
g.summarize_scores()
plt.plot(list(g.scoresCount.values()))
plt.show()
stat, p_value = shapiro(list(g.scoresCount.values()))
print(f'Statystyka testu: {stat}, P-wartość: {p_value}')
plt.hist(list(g.scoresCount.values()), bins=20, density=True, alpha=0.5)
