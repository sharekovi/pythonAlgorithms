def bubble_sort_descending(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, no need to compare them
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [14, 25, 11, 23, 111]
print(bubble_sort_descending(arr))
