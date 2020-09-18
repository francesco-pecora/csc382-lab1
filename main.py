from generators.generators import Generator
from algorithms.mergeSort import mergeSort
from algorithms.insertionSort import insertionSort
from visualization.visualize import Visualizer
import time

def runInsertionSort(arr):
    startTime = time.perf_counter()
    steps = insertionSort(arr)
    endTime = time.perf_counter()
    return (endTime - startTime) * 1000000, steps

def runMergeSort(arr):
    startTime = time.perf_counter()
    _, steps = mergeSort(arr, 0)
    endTime = time.perf_counter()
    return (endTime - startTime) * 1000000, steps

def runSortedArrays(inputs):
    insertionTimes = []     # cpu time for insertion sort
    insertionSteps = []     # num of operations for insertion sort
    mergeTimes = []         # cpu time for merge sort
    mergeSteps = []         # num of operations for insertions sort

    for inputSize in inputs:
        generator = Generator(inputSize)
        newArray = generator.generateSortedArray()
        insertionTime, insertionStep = runInsertionSort(newArray)
        
        newArray = generator.generateSortedArray()
        mergeTime, mergeStep = runMergeSort(newArray)
        
        insertionTimes.append(insertionTime)
        insertionSteps.append(insertionStep)

        mergeTimes.append(mergeTime)
        mergeSteps.append(mergeStep)

    return insertionTimes, insertionSteps, mergeTimes, mergeSteps

def runReversedSortedArrays(inputs):
    insertionTimes = []     # cpu time for insertion sort
    insertionSteps = []     # num of operations for insertion sort
    mergeTimes = []         # cpu time for merge sort
    mergeSteps = []         # num of operations for insertions sort

    for inputSize in inputs:
        generator = Generator(inputSize)
        newArray = generator.generateReversedSortedArray()
        insertionTime, insertionStep = runInsertionSort(newArray)
        
        newArray = generator.generateReversedSortedArray()
        mergeTime, mergeStep = runMergeSort(newArray)
        
        insertionTimes.append(insertionTime)
        insertionSteps.append(insertionStep)

        mergeTimes.append(mergeTime)
        mergeSteps.append(mergeStep)

    return insertionTimes, insertionSteps, mergeTimes, mergeSteps

def runRandomPermutationArrays(inputs):
    insertionTimes = []     # cpu time for insertion sort
    insertionSteps = []     # num of operations for insertion sort
    mergeTimes = []         # cpu time for merge sort
    mergeSteps = []         # num of operations for insertions sort

    for inputSize in inputs:
        generator = Generator(inputSize)
        newArray = generator.generateRandomPermutation()
        insertionTime, insertionStep = runInsertionSort(newArray)
        
        newArray = generator.generateRandomPermutation()
        mergeTime, mergeStep = runMergeSort(newArray)
        
        insertionTimes.append(insertionTime)
        insertionSteps.append(insertionStep)

        mergeTimes.append(mergeTime)
        mergeSteps.append(mergeStep)

    return insertionTimes, insertionSteps, mergeTimes, mergeSteps


if __name__ == '__main__':

    inputs = [100, 200, 300, 400, 500, 1000, 2000, 4000, 10000]
    print()

    visualizer = Visualizer(inputs)

    # running algorithms for the sorted array inputs
    insertionTimes, insertionSteps, mergeTimes, mergeSteps = runSortedArrays(inputs)
    print('- SORTED ARRAYS -')
    print()
    visualizer.printSingleRunValues(insertionTimes, insertionSteps, mergeTimes, mergeSteps)
    visualizer.plotCurves(inputs, insertionTimes, mergeTimes)

    print('[STILL RUNNING] wait for the new output...')
    print()

    # running algorithms for the reversed sorted array inputs
    insertionTimes, insertionSteps, mergeTimes, mergeSteps = runReversedSortedArrays(inputs)
    print('- REVERSED SORTED ARRAYS -')
    print()
    visualizer.printSingleRunValues(insertionTimes, insertionSteps, mergeTimes, mergeSteps)
    visualizer.plotCurves(inputs, insertionTimes, mergeTimes)

    print('[STILL RUNNING] wait for the new output...')
    print()

    # running algorithms for the random permutation array inputs
    insertionTimes, insertionSteps, mergeTimes, mergeSteps = runReversedSortedArrays(inputs)
    print('- RANDOM PERMUTATION ARRAYS -')
    print()
    visualizer.printSingleRunValues(insertionTimes, insertionSteps, mergeTimes, mergeSteps)
    visualizer.plotCurves(inputs, insertionTimes, mergeTimes)