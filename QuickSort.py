def partition(arr, low, high):
    pivot = arr[(low+high)//2]
    i = low-1
    j = high+1

    while(True):
        i += 1
        while(arr[i] < pivot):
            i += 1
        j -= 1
        while(arr[j] > pivot):
            j -= 1

        if(i >= j):
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quickSort(arr):

    def quickSortHelper(arr, low, high):
        if(low < high):
            splitIndex = partition(arr, low, high)
            quickSortHelper(arr, low, splitIndex)
            quickSortHelper(arr, splitIndex+1, high)

    quickSortHelper(arr, 0, len(arr)-1)


list_of_numbers = [90, 790, 345, 234, 123, 657, 456]
quickSort(list_of_numbers)
print(list_of_numbers)


# WORST CASE TIME COMPLEXITY O(n^2)
# AVERAGE TIME COMPLEXITY O(nlogn)
