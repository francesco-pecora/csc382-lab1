def mergesort(arr):

    if len(arr) == 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        else:
            return arr

    p = len(arr)//2
    m1 = mergesort(arr[:p])
    m2 = mergesort(arr[p:])

    result = []
    while 1:
        if len(m1) > 0 and len(m2) > 0:
            if m1[0] <= m2[0]:
                result.append(m1[0])
                m1 = m1[1:]
            else:
                result.append(m2[0])
                m2 = m2[1:]
        elif len(m1) > 0:
            result += m1
            m1 = []
        elif len(m2) > 0:
            result += m2
            m2 = []
        else:
            break
    return result

if __name__ == '__main__':
    a = [5,9,1,3,4,6,6,3,2]
    print(mergesort(a))