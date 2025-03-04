unsorted = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]

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
print(unsorted)