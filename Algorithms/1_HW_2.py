# 2. Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.


# 0(1)
def find_max(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c


test_result = find_max(14, 22, 36)
print(test_result)


