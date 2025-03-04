import pandas as pd

import time

csv = pd.read_excel("rugby_players_data.xlsx")

age = csv["Age"].tolist()

delay = 0.001

start_time = time.time()

unsorted = age
# unsorted = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]

def bubblesort():
    while True:
        swap = False
        currentnumber = 0
        previousnumber = 0
        previousindex = 0

        for currentindex, number in enumerate(unsorted):
            currentnumber = number
            if previousnumber > currentnumber:
                unsorted[currentindex], unsorted[previousindex] = unsorted[previousindex], unsorted[currentindex]
                swap = True
            previousnumber = currentnumber
            previousindex = currentindex
        if swap == False:
            break
bubblesort()
# print(unsorted)

time.sleep(delay)
end_time = time.time()

print(f"It took {end_time - start_time - delay:.6f} seconds to run BubbleSort") 


start_time = time.time()

def insertionsort():
    length = len(unsorted)
    for currentindex in range(1, length):
        insertposition = currentindex
        currentvalue = unsorted.pop(currentindex)
        for previousindex in range(currentindex - 1, -1, -1):
            if unsorted[previousindex] > currentvalue:
                insertposition = previousindex
        unsorted.insert(insertposition, currentvalue)

insertionsort()
# print(unsorted)

time.sleep(delay)
end_time = time.time()

print(f"It took {end_time - start_time - delay:.6f} seconds to run InsertionSort") 


start_time = time.time()

def selectionsort():
    length = len(unsorted)
    for currentindex in range(length - 1):
        smallestindex = currentindex
        for nextindex in range(currentindex + 1, length):
            if unsorted[nextindex] < unsorted[smallestindex]:
                smallestindex = nextindex
        smallestvalue = unsorted.pop(smallestindex)
        unsorted.insert(currentindex, smallestvalue)
selectionsort()
# print(unsorted)

time.sleep(delay)
end_time = time.time()

print(f"It took {end_time - start_time - delay:.6f} seconds to run SelectionSort") 


start_time = time.time()

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
        # print(number, end=" ")
        continue
    # print()

if __name__ == "__main__":
    printarray(unsorted)

    mergesort(unsorted, 0, len(unsorted) - 1)

    printarray(unsorted)

time.sleep(delay)
end_time = time.time()

print(f"It took {end_time - start_time - delay:.6f} seconds to run MergeSort") 


start_time = time.time()

def quicksort_iterative(numbers):
    if len(numbers) <= 1:
        return numbers
    
    stack = [(0, len(numbers) - 1)]
    
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        
        pivot_index = partition(numbers, start, end)
        
        stack.append((start, pivot_index - 1))
        stack.append((pivot_index + 1, end))

    return numbers

def partition(numbers, start, end):
    pivot_value = numbers[end]
    partition_index = start - 1

    for current_index in range(start, end):
        if numbers[current_index] < pivot_value:
            partition_index += 1
            numbers[partition_index], numbers[current_index] = numbers[current_index], numbers[partition_index]
    
    numbers[partition_index + 1], numbers[end] = numbers[end], numbers[partition_index + 1]
    return partition_index + 1

sorted_numbers = quicksort_iterative(unsorted)
# print("Sorted array:", sorted_numbers)

time.sleep(delay)
end_time = time.time()

print(f"It took {end_time - start_time - delay:.6f} seconds to run QuickSort") 


start_time = time.time()

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
        # print(num, end=" ")
        continue
    # print()

heapsort(unsorted)
# print("Sorted array is:")
printarray(unsorted)

time.sleep(delay)
end_time = time.time()

print(f"It took {end_time - start_time - delay:.6f} seconds to run HeapSort") 