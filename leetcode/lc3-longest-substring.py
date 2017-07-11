"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description
topics: PYTHON DICTIONARY (HASH MAP)
difficulty: medium

Given a string, find the length of the longest substring without repeating
characters. 

Examples:
given "abcabcbb" --> longest substring is "abc", so answer is 3
given "bbbbb" --> longest substring is "b", so answer is 1
given "pwwkew" --> longest substring is "wke", so answer is 3

"""

# Solution from Leetcode.com using HASH MAP (Python dictionary)
# "Sliding Window Optimized" solution
# i and j move along the string. i stops at start of substring to find where
# a substring between i and j would be longest
def soln(s):
    len_longest = 0
    chars_seen = {}
    i = 0
    for j in range(0, len(s)):
        if s[j] in chars_seen:
            i = max(chars_seen[s[j]], i)
        len_longest = max(len_longest, j - i + 1)
        chars_seen[s[j]] = j + 1

    return len_longest

print soln("12ertert123")



# my initial algorithm:
# initiate empty string to store longest substring seen
# initiate empty string to store current substring
# for each character in string
#     check if character has been seen in current substring of unique chars
#     if it hasn't been seen, add it to the current substring
#     if it has been seen, save the length of the current substring
#     (if longer than current longest) and restart substring to contain current char
# return length of longest substring

def longest_substring(s):
    longest_substr = ""
    curr_substr = ""
    for char in s:
        if char in curr_substr:
            if len(curr_substr) > len(longest_substr):
                longest_substr = curr_substr
            curr_substr = char
        else:
            curr_substr += char    
    if len(curr_substr) > len(longest_substr):
        longest_substr = curr_substr
    return longest_substr, len(longest_substr)

# print longest_substring("aabcda")
