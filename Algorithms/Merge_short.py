def merge_sort_descending(arr):
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2

        # Dividing the array elements into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Sorting the first half
        merge_sort_descending(left_half)

        # Sorting the second half
        merge_sort_descending(right_half)

        i = j = k = 0

        # Merge the two halves back into the array
        while i < len(left_half) and j < len(right_half):
            # For descending order, change left_half[i] < right_half[j] to left_half[i] > right_half[j] below
            if left_half[i] > right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left in the two halves
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


arr = [73, 215, 1322, 122, 911]
print(merge_sort_descending(arr))
