# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def find_two_lowest(arr):
    arr.sort()
    return arr[:2]


test_list = [3, 7, 2, 1, 10, 97, 4]     # [1,2]
result = find_two_lowest(test_list)
print(result)
