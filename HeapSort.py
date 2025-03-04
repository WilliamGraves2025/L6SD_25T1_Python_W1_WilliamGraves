def heapify(numbers, heapsize, rootindex):

    largestindex = rootindex
    leftchildindex = 2 * rootindex + 1
    rightchildindex = 2 * rootindex + 2

    if leftchildindex < heapsize and numbers[leftchildindex] > numbers[largestindex]:
        largestindex = leftchildindex

    if rightchildindex < heapsize and numbers[rightchildindex] > numbers[largestindex]:
        largestindex = rightchildindex

    if largestindex != rootindex:
        numbers[rootindex], numbers[largestindex] = numbers[largestindex], numbers[rootindex]
        heapify(numbers, heapsize, largestindex)

def heapsort(numbers):
    size = len(numbers)

    for index in range(size // 2 - 1, -1, -1):
        heapify(numbers, size, index)

    for index in range(size - 1, 0, -1):
        numbers[0], numbers[index] = numbers[index], numbers[0]
        heapify(numbers, index, 0)

def printarray(numbers):
    for num in numbers:
        print(num, end=" ")
    print()

unsortednumbers = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]
heapsort(unsortednumbers)
print("Sorted array is:")
printarray(unsortednumbers)