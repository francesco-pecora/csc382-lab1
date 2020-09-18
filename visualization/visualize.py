import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np

class Visualizer:

    def __init__(self, inputs):
        self.inputs = inputs

    def printSingleRunValues(self, insertionTimes, insertionSteps, mergeTimes, mergeSteps):
        '''
        function that prints information about each run of the two algorithms
        insertionTimes -> list of CPU times for insertion sort
        insertionSteps -> list of operations during insertion sort
        mergeTimes -> list of CPU times for merge sort
        '''
        for i in range(len(self.inputs)):
            print('Input Size: ', self.inputs[i])
            print('Insertion CPU Time: ', insertionTimes[i], 'x 10^(-2) seconds')
            print('Insertion Steps: ', insertionSteps[i])
            print('C constant: ', float(insertionSteps[i]) / (self.inputs[i] ** 2.0))
            print('Merge CPU Time: ', mergeTimes[i], 'x 10^(-2) seconds')
            print('Merge Steps: ', mergeSteps[i])
            print('C constant: ', float(mergeSteps[i]) / (self.inputs[i] ** 2.0))
            print()

    
    def plotCurves(self, x, y, z, title):

        x = [x*100 for x in range(1, len(x) + 1)]

        _, axs = plt.subplots(3)

        axs[0].plot(x, y, 'r', label='Insertion Curve')
        axs[1].plot(x, z, 'b', label='Merge Curve')
        axs[2].plot(x, y, 'r', label='Insertion Curve')
        axs[2].plot(x, z, 'b', label='Merge Curve')

        plt.xlabel('Number of Operations')
        plt.ylabel('CPU Time')

        axs[0].set_title('Insertion Sort')
        axs[1].set_title('Merge Sort')
        axs[2].set_title('Insertion + Merge')

        axs[0].legend()
        axs[1].legend()
        axs[2].legend()
        plt.legend()
        plt.tight_layout()
        plt.show()
        '''
        plt.plot(x, y, x, z)
        
        plt.xlabel('Number of Operations')
        plt.ylabel('CPU Time')

        plt.xticks(x)
        plt.legend()
        plt.show()
        '''
