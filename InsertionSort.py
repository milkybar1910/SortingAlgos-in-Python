def insertionSort(arr):
    for i in range(1, len(arr)-1):
        itemToInsert = arr[i]
        j = i-1

        while(j >= 0 and arr[j] > itemToInsert):
            arr[j+1] = itemToInsert
            j -= 1
        arr[j+1] = itemToInsert


list_of_numbers = [5, 12, 45, 78, 23]
insertionSort(list_of_numbers)
print(list_of_numbers)

# Time Complexity : O(n^2)
