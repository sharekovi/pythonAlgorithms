# When given a list, the program should return a list of all the elements below the original list’s arithmetical
# mean. The arithmetical mean is the sum of all elements divided by the number of elements. Example: [1, 3, 5, 6, 4,
# 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

# 0(n)
def below_am(arr):
    am = sum(arr) / len(arr)
    final_result = []
    for x in arr:
        if x < am:
            final_result.append(x)
    return final_result


test_list =[1, 3, 5, 6, 4, 10,2,3]  # am = 4.25, result = [ 1,3,4,2,3]
test_list = below_am(test_list)
print(test_list)

