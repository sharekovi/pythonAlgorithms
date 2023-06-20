# Increment a Number Write a program that takes as input a list of digits encoding a nonnegative decimal integer D
# and updates the list to represent the integer D + 1. For example, if the input is [1, 2, 9] then you should update
# the list to [1, 3, 0].


# [1,2,5] => [1,2,6]
# [1,2,9] => [1,3,0]
# [1,9,9] => [2,0,0]
# [9,9,9] => [1,0,0,0]

# 0(n)
def plus_one(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
            arr[1] = 0
            arr[i - 1] += 1

        if arr[0] == 10:
            arr[0] = 1
            arr.append(0)
        print(arr)

        test1 = [1, 2, 5]      # =>[1,2,6]
        plus_one(test1)
        test2 = [1, 2, 9]      # =>[1,3,0]
        plus_one(test2)
        test3 = [1, 9, 9]      # =>[1,3,0]
        plus_one(test3)
        test4 = [9, 9, 9]      # =>[2,0,0]
        plus_one(test4)
