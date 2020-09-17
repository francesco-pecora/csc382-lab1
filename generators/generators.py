import random

class Generator:

    def __init__(self, n):
        self.n = n

    def generateSortedArray(self):
        '''
        function that returns an array of numbers from 1 to n
        '''
        sortedArr = []
        # lab instructions exlude 0 and include n
        for i in range(1, self.n + 1):
            sortedArr.append(i)
        return sortedArr


    def generateReversedSortedArray(self):
        '''
        function that returns an array of numbers from n to 1
        '''
        sortedArr = []
        # lab instructions exlude 0 and include n
        for i in reversed(range(1, self.n + 1)):
            sortedArr.append(i)
        return sortedArr


    def generateRandomPermutation(self):
        '''
        function that returns an array of a random permutation between 1 and n
        '''
        sortedArr = self.generateSortedArray()
        random.shuffle(sortedArr)
        return sortedArr


    def generate50RandomInRange(self):
        '''
        function that generates an array of 50 arrays of n random numbers in the range 1 to n
        '''
        arrays = []
        for _ in range(50):
            newArr = []
            for _ in range(self.n):
                newArr.append(random.randint(1, self.n))
            arrays.append(newArr)
        return arrays



if __name__ == '__main__':
    generator = Generator(10)
    print(generator.generateRandomPermutation())