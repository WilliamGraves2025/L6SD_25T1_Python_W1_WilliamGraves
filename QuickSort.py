def partition(numbers, start, end):
    pivotvalue = numbers[end]
    partitionindex = start - 1

    for currentindex in range(start, end):
        if numbers[currentindex] <= pivotvalue:
            partitionindex += 1
            numbers[partitionindex], numbers[currentindex] = numbers[currentindex], numbers[partitionindex]

    numbers[partitionindex + 1], numbers[end] = numbers[end], numbers[partitionindex + 1]
    return partitionindex + 1

def quicksort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers) -1

    if start < end:
        pivotindex = partition(numbers, start, end)
        quicksort(numbers, start, pivotindex - 1)
        quicksort(numbers, pivotindex + 1, end)

unsortednumbers = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]
quicksort(unsortednumbers)
print("Sorted array:", unsortednumbers)