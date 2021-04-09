def heapify(arr, heapSize, root):

    largest = root
    left = root+1
    right = root+2

    if(left < heapSize and arr[left] > arr[largest]):
        largest = left

    if(right < heapSize and arr[right] > arr[largest]):
        largest = right

    if(largest != root):
        arr[largest], arr[root] = arr[root], arr[largest]
        heapify(arr, heapSize, largest)


def heapSort(arr):

    n = len(arr)

    for i in range(n-1, -1, -1):
        heapify(arr, n, i)

    # [90 78 45 32 12]

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


list_of_numbers = [12, 78, 32, 45, 90]
heapSort(list_of_numbers)
print(list_of_numbers)

# Time Complexity : O(nlogn)
