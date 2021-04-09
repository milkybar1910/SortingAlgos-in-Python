def merge(leftList, rightList):

    leftListLength, rightListLength = len(leftList), len(rightList)

    leftIndex = rightIndex = 0

    sortedArray = []

    for _ in range(leftListLength+rightListLength):

        if(leftIndex < leftListLength and rightIndex < rightListLength):
            if(leftList[leftIndex] <= rightList[rightIndex]):
                sortedArray.append(leftList[leftIndex])
                leftIndex += 1
            else:
                sortedArray.append(rightList[rightIndex])
                rightIndex += 1

        elif(leftIndex == leftListLength):
            sortedArray.append(rightList[rightIndex])
            rightIndex += 1
        elif(rightIndex == rightListLength):
            sortedArray.append(leftList[leftIndex])
            leftIndex += 1
    return sortedArray


def mergeSort(arr):

    if(len(arr) <= 1):
        return arr

    mid = len(arr)//2

    leftList = mergeSort(arr[:mid])
    rightList = mergeSort(arr[mid:])

    return merge(leftList, rightList)


list_of_numbers = [56, 12, 89, 400, 560]
list_of_numbers = mergeSort(list_of_numbers)
print(list_of_numbers)

# Time Complexity : O(nlogn)
