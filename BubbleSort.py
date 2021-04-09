

def bubblesort(arr):
    swapped = True
    while(swapped):
        swapped = False
        for i in range(0, len(arr)-1):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True


list_of_numbers = [5, 2, 8, 10, 1]
bubblesort(list_of_numbers)
print(list_of_numbers)

# Time Complexity : O(n^2)
