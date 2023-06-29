def selection_sort_descending(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the maximum element in remaining unsorted array
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j

        # Swap the found maximum element with the first element of the 'unsorted' part
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


arr = [644, 251, 132, 252, 311]
print(selection_sort_descending(arr))
