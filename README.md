# Dartboard Simulator

This project simulates dart throws on two distinct types of dartboards, employing Python and various statistical methods for analysis.
Overview

The repository contains two classes, Dartboard_1 and Dartboard_2, representing different dartboards.

  1. Dartboard_1 calculates throw placement based on x and y coordinates within the board.
  2. Dartboard_2 uses radius and angle for throw placement.

## Features

- Simulation: Simulates a series of throws on both dartboards.
- Visualization: Generates visual representations of the dartboards, displaying the throw distribution.
<p>
  <img src='https://github.com/poolinaaa/dart-simulation-repo/assets/125304122/8bdef37d-d176-4055-a855-da4bef703e49' width=400 height=400>       <img src='https://github.com/poolinaaa/dart-simulation-repo/assets/125304122/c873cf81-157f-4637-b26b-a8032a6962aa', width=400px height=400px>
</p>   

- Statistical Analysis: Compares the average scores between the two dartboards using statistical tests.


## Statistical Testing

The test_distributions function conducts statistical tests to compare the average scores between the two dartboards. It employs t-tests and non-parametric test (Mann-Whitney U test) to determine statistical significance.

example outcome: 

![obraz](https://github.com/poolinaaa/dart-simulation-repo/assets/125304122/fdaecdf8-0090-4f35-96f8-8e550c04d38a)

## Customization Options
1. Number of Throws

Modify the number of throws to simulate different scenarios by adjusting the nrOfRounds parameter in the simulate method. 

2. Significance Level

Alter the significance level for statistical testing by changing the alpha value in the test_distributions function. This value determines the threshold for significance in the comparison between dartboards.

3. Dartboard Radius

Adjust the radius of the dartboard for different gameplay experiences. You can modify the radius of the dartboard by altering the radiusOfBoard attribute in each Dartboard class.


### Example Usage

Customize the simulation according to your preferences by tweaking these parameters. For instance, you can simulate a higher number of throws, adjust the significance level for hypothesis testing, and change the size of the dartboards to observe varied outcomes and statistical insights.

    
    #Customized Simulation Example
    playFirstDartboard = Dartboard_1()
    playFirstDartboard.radiusOfBoard = 0.6
    playFirstDartboard.simulate(500)
    
    playSecondDartboard = Dartboard_2()
    playSecondDartboard.radiusOfBoard = 1.2
    playSecondDartboard.simulate(500)
    
    test_distributions(playFirstDartboard, playSecondDartboard, alpha=0.01)


### Adapting the Project

Feel free to adjust these parameters to explore different scenarios and test hypotheses based on varying numbers of throws, significance levels, and dartboard sizes. Tailor the simulation to your specific needs for in-depth analysis and experimentation.


## Used technology

- Python
- scipy, matplotlib
