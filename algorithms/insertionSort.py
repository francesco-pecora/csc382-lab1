import random

def insertionSort(arr):
    '''
    Sorting algorithm. Time O(n^2) Space O(1)
    '''

    # initialization of i to 1
    numSteps = 1

    for i in range(1, len(arr)):
        
        # boolean comparison, incrementing i by 1
        numSteps += 2

        key = arr[i]
        j = i-1

        # assigning the value of key and the value of j
        numSteps += 2

        while j >=0 and key < arr[j]:

            # two logical comparisons
            numSteps += 2

            arr[j+1] = arr[j]
            j -= 1

            # assignment operaton and decrement j by 1
            numSteps += 2

        arr[j+1] = key

        # assigning the key to the right position
        numSteps += 1

    return numSteps

if __name__ == '__main__':
    n = 100
    a = [random.randint(1, n) for _ in range(1, n + 1)]
    a = [x for x in range(1, n+ 1)]
    finalSteps = insertionSort(a)
    print(a, ' -> ', finalSteps)