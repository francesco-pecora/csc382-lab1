def insertionSort(arr):
    '''
    Sorting algorithm. Time O(n^2) Space O(1)
    '''
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

if __name__ == '__main__':
    a = [5,9,1,3,4,6,6,3,2]
    insertionSort(a)
    print(a)