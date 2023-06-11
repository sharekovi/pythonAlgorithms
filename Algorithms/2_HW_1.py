# 1. Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'iiiiioooov'. Result = ‘0000vvvvi’.

# 0(1)
def split_in_half(s):
    length = len(s)
    half = length // 2
    add = 0
    if length % 2:
        add = 1
    left = s[:half + add]
    right = s[half + add:]
    return right + left


test_string_odd = "oooviii"  # iiiooov
test_string_even = "ooovvv"  # vvvooo
print(split_in_half(test_string_odd))
print(split_in_half(test_string_even))
