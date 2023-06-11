# 2. Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.



# 0(1)
def unique_char_star(s):
    lenstr = len(s)
    lenset = len(set(s))
    return lenset == lenstr


test_data_pos = "abcde"  # true
test_data_neg = "abcdee"  # false"
print(unique_char_star(test_data_pos))
print(unique_char_star(test_data_neg))
