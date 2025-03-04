def merge(array, start, middle, end):
    leftsize = middle - start + 1
    rightsize = end - middle

    leftsubarray = [0] * leftsize
    rightsubarray = [0] * rightsize

    for leftindex in range(leftsize):
        leftsubarray[leftindex] = array[start + leftindex]

    for rightindex in range(rightsize):
        rightsubarray[rightindex] = array[middle + 1 + rightindex]

    leftindex = 0
    rightindex = 0
    mergedindex = start

    while leftindex < leftsize and rightindex < rightsize:
        if leftsubarray[leftindex] <= rightsubarray[rightindex]:
            array[mergedindex] = leftsubarray[leftindex]
            leftindex += 1
        else:
            array[mergedindex] = rightsubarray[rightindex]
            rightindex += 1
        mergedindex += 1

    while leftindex < leftsize:
        array[mergedindex] = leftsubarray[leftindex]
        leftindex += 1
        mergedindex += 1

    while rightindex < rightsize:
        array[mergedindex] = rightsubarray[rightindex]
        rightindex += 1
        mergedindex += 1

def mergesort(array, start, end):
    if start < end:
        middle = (start + end) // 2

        mergesort(array, start, middle)
        mergesort(array, middle + 1, end)
        merge(array, start, middle, end)

def printarray(array):
    for number in array:
        print(number, end=" ")
    print()

if __name__ == "__main__":
    numbers = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]
    print("Given array is:")
    printarray(numbers)

    mergesort(numbers, 0, len(numbers) - 1)

    print("\nSorted array is:")
    printarray(numbers)