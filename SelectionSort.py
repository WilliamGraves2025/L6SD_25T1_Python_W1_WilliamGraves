unsorted = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]

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
print(unsorted)