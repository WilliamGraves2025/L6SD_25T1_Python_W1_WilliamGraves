unsorted = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]

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
print(unsorted)