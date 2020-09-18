import random

def mergeSort(arr, numSteps):
    '''
    implementation of merge sort with the
    addition of counting the number of operations
    '''

    if len(arr) == 1:
        # counting one comparison in the if statement
        numSteps += 1
        return arr, numSteps
    
    elif len(arr) == 2:
        # counting one comparison in the if statement
        numSteps += 1
        
        if arr[0] > arr[1]:
            # counting one comparison in the if statement
            numSteps += 1
            return [arr[1], arr[0]], numSteps
        else:
            # counting one comparison in the if statement (when the if is false, this is immediately run)
            numSteps += 1
            return arr, numSteps

    p = len(arr)//2

    # counting the assignment of p
    numSteps += 1

    m1, _ = mergeSort(arr[:p], numSteps)
    m2, _ = mergeSort(arr[p:], numSteps)

    # counting the assignments of m1 and m2 
    numSteps += 1
    numSteps += 1

    result = []

    # counting the allocation of result
    numSteps += 1

    while True:
        if len(m1) > 0 and len(m2) > 0:

            # counting the two logical comparisons
            numSteps += 2

            if m1[0] <= m2[0]:
                # counting the logical comparison
                numSteps += 1
                result.append(m1[0])
                m1 = m1[1:]
                # counting the assignment of m1 and the update of result
                numSteps += 2
            else:
                # counting the logical comparison
                numSteps += 1
                result.append(m2[0])
                m2 = m2[1:]
                # counting the assignment of m2 and the update of result
                numSteps += 2
        elif len(m1) > 0:
            # counting the logical comparisons (the first if and this elif)
            numSteps += 2
            result += m1
            m1 = []
            # counting the assignment of m1 and the update of result
            numSteps += 2
        elif len(m2) > 0:
            # counting the logical comparisons (the first if, the elif, and the current elif)
            numSteps += 3
            result += m2
            m2 = []
            # counting the assignment of m2 and the update of result
            numSteps += 2
        else:
            # counting the logical comparisons
            numSteps += 3
            break
    return result, numSteps

if __name__ == '__main__':
    '''
    testing purposes
    '''
    n = 100
    a = [random.randint(1, n) for _ in range(1, n + 1)]
    a = [x for x in reversed(range(1, n+ 1))]
    sortedList, steps = mergeSort(a, 0)
    print(sortedList, steps)