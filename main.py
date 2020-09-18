from generators.generators import Generator
from algorithms.mergeSort import mergeSort
from algorithms.insertionSort import insertionSort
from visualization.visualize import Visualizer
import time


def runInsertionSort(arr):
    '''
    function that runs and times insertion sort
    arr -> list of integers
    return -> time in seconds^(-5), num of operations
    '''
    # returns time in nano seconds
    startTime = time.perf_counter_ns()
    steps = insertionSort(arr)
    endTime = time.perf_counter_ns()
    return (endTime - startTime) / 10000000.0, steps


def runMergeSort(arr):
    '''
    function that runs and times merge sort
    arr -> list of integers
    return -> time in seconds^(-5), num of operations
    '''
    startTime = time.perf_counter_ns()
    _, steps = mergeSort(arr, 0)
    endTime = time.perf_counter_ns()
    return (endTime - startTime) / 10000000.0, steps


def runSortedArrays(inputs):
    '''
    function that performs multiple runs on both insertion
    sort and merge sort using sorted arrays as input for the sort
    inputs -> array of input sizes
    return -> info about the two algorithm runs (time and steps for each one)
    '''
    insertionTimes = []     # cpu time for insertion sort
    insertionSteps = []     # num of operations for insertion sort
    mergeTimes = []         # cpu time for merge sort
    mergeSteps = []         # num of operations for merge sort

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
    '''
    function that performs multiple runs on both insertion
    sort and merge sort using reversed sorted arrays as input for the sort
    inputs -> array of input sizes
    return -> info about the two algorithm runs (time and steps for each one)
    '''
    insertionTimes = []     # cpu time for insertion sort
    insertionSteps = []     # num of operations for insertion sort
    mergeTimes = []         # cpu time for merge sort
    mergeSteps = []         # num of operations for merge sort

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
    '''
    function that performs multiple runs on both insertion
    sort and merge sort using random permutations as input for the sort
    inputs -> array of input sizes
    return -> info about the two algorithm runs (time and steps for each one)
    '''
    insertionTimes = []     # cpu time for insertion sort
    insertionSteps = []     # num of operations for insertion sort
    mergeTimes = []         # cpu time for merge sort
    mergeSteps = []         # num of operations for merge sort

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


def run50RandomInRangeArrays(inputs):
    '''
    function that generates n arrays of n random numbers (n is each entry in inputs)
    and returns info about the runs in the form of average of the n runs
    inputs -> list of array sizes
    return -> average info about the two algorithm runs (time and steps for each one)
    '''
    finalInsertionTimes = []     # cpu time for insertion sort
    finalInsertionSteps = []     # num of operations for insertion sort
    finalMergeTimes = []         # cpu time for merge sort
    finalMergeSteps = []         # num of operations for merge sort
    for inputSize in inputs:
        insertionTimes = []
        insertionSteps = []
        mergeTimes = []
        mergeSteps = []
        generator = Generator(inputSize)
        arrays = generator.generate50RandomInRange()
        for array in arrays:
            mergeTime, mergeStep = runMergeSort(array)
            mergeTimes.append(mergeTime)
            mergeSteps.append(mergeStep)

            insertionTime, insertionStep = runInsertionSort(array)
            insertionTimes.append(insertionTime)
            insertionSteps.append(insertionStep)
        
        # appending the average of the n runs in the final result array
        finalInsertionTimes.append(sum(insertionTimes)/len(insertionTimes))
        finalInsertionSteps.append(sum(insertionSteps)/len(insertionSteps))
        finalMergeTimes.append(sum(mergeTimes)/len(mergeTimes))
        finalMergeSteps.append(sum(mergeSteps)/len(mergeSteps))
    
    return finalInsertionTimes, finalInsertionSteps, finalMergeTimes, finalMergeSteps


if __name__ == '__main__':

    # input sizes given in the instructions
    inputs = [100, 200, 300, 400, 500, 1000, 4000, 10000]
    print()

    visualizer = Visualizer(inputs)

    # running algorithms for the sorted array inputs
    insertionTimes, insertionSteps, mergeTimes, mergeSteps = runSortedArrays(inputs)
    print('- SORTED ARRAYS -')
    print()
    visualizer.printSingleRunValues(insertionTimes, insertionSteps, mergeTimes, mergeSteps)
    visualizer.plotCurves(inputs, insertionTimes, mergeTimes, 'SORTED ARRAYS')

    print('[STILL RUNNING] wait for the new output...')
    print()

    # running algorithms for the reversed sorted array inputs
    insertionTimes, insertionSteps, mergeTimes, mergeSteps = runReversedSortedArrays(inputs)
    print('- REVERSED SORTED ARRAYS -')
    print()
    visualizer.printSingleRunValues(insertionTimes, insertionSteps, mergeTimes, mergeSteps)
    visualizer.plotCurves(inputs, insertionTimes, mergeTimes, 'REVERSED SORTED ARRAYS')

    print('[STILL RUNNING] wait for the new output...')
    print()

    # running algorithms for the random permutation array inputs
    insertionTimes, insertionSteps, mergeTimes, mergeSteps = runReversedSortedArrays(inputs)
    print('- RANDOM PERMUTATION ARRAYS -')
    print()
    visualizer.printSingleRunValues(insertionTimes, insertionSteps, mergeTimes, mergeSteps)
    visualizer.plotCurves(inputs, insertionTimes, mergeTimes, 'RANDOM PERMUTATION ARRAYS')

    print('[STILL RUNNING] wait for the new output...')
    print()

    # running algorithms for the random permutation array inputs
    insertionTimes, insertionSteps, mergeTimes, mergeSteps = run50RandomInRangeArrays(inputs)
    print('- 50 RANDOM ARRAYS EACH RUN -')
    print()
    visualizer.printSingleRunValues(insertionTimes, insertionSteps, mergeTimes, mergeSteps)
    visualizer.plotCurves(inputs, insertionTimes, mergeTimes, '50 RANDOM ARRAYS EACH RUN')