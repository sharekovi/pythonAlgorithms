# 1 .Compute the sum of digits in all numbers from 1 to n.
# When a function gets a number n, find the sum of digits in
# all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15


# 0(1)
def sumn(n):
    final_sum = 0
    for x in range(n + 1):
        final_sum += x
        return final_sum

    test_data = 5
    test_result = sumn(test_data)
    print(test_result)

