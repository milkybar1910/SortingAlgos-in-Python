def selectionSort(arr):
    for i in range(0, len(arr)):
        lowIndex = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[lowIndex]):
                lowIndex = j
        arr[i], arr[lowIndex] = arr[lowIndex], arr[i]


list_of_numbers = [4, 23, 9, 8, 5]
selectionSort(list_of_numbers)
print(list_of_numbers)

# Time Complexity : O(n^2)
