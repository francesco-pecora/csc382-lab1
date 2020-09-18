import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np

class Visualizer:

    def __init__(self, inputs):
        self.inputs = inputs

    def printSingleRunValues(self, insertionTimes, insertionSteps, mergeTimes, mergeSteps):
        for i in range(len(self.inputs)):
            print('Input Size: ', self.inputs[i])
            print('Insertion CPU Time: ', insertionTimes[i], 'x 10^(-5) seconds')
            print('Insertion Steps: ', insertionSteps[i])
            print('Merge CPU Time: ', mergeTimes[i], 'x 10^(-5) seconds')
            print('Merge Steps: ', mergeSteps[i])
            print()

    def exponentialFit(self, x, a, b, c):
        return a*np.exp(-b*x) + c

    def plotCurves(self, x, y, z):

        # data spans across this range in the x axis
        x = np.array([x for x in range(0, len(x))])

        # parameters for fitting curve with insertion sort data
        fitting_parameters, _ = optimize.curve_fit(self.exponentialFit, x, y)
        a, b, c = fitting_parameters

        plt.plot(x, self.exponentialFit(x, a, b, c), '-', label='Insertion Fit')

        # parameters for fitting curve with merge sort data
        fitting_parameters, _ = optimize.curve_fit(self.exponentialFit, x, z)
        a, b, c = fitting_parameters

        plt.plot(x, self.exponentialFit(x, a, b, c), '-', label='Merge Fit')

        plt.xticks(x)   # input given in the instructions are marked
        plt.legend()
        plt.show()
