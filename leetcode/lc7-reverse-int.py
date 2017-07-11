"""
https://leetcode.com/problems/reverse-integer/#/description
difficulty: easy

Reverse the digits of an integer.

Examples:
Given 123, return 321
Given -123, return -321
Given 100, return 1

"""

def reverse_int(x):
    # neg: is x negative?
    neg = x < 0
    st = str(abs(x))
    rev_str = st[::-1]
    ans = int(rev_str)
    if neg == True:
        ans = ans * -1
    return ans

# test
# t = 3345
# t = 1000
t = -78
# t = 0
print reverse_int(t)


####################
# another user's solution (with my notes)
def reverse(x):
    # cmp() returns 1 if first val is greater than second,
    # returns 0 if equal, and returns -1 if less than
    # what s is doing is determining if x is a positive or negative number
    
    # backticks make s*x a string, and the slicing notation reverses the string
    
    # instructions indicate to return 0 if the integer will overflow
    # the boolean r < 2*31 determines if it will and then multiplying s*r
    # by the False will return 0. Otherwise, if True, it'll return the reversed int

    s = cmp(x, 0)
    r = int(`s*x`[::-1])
    return s*r * (r < 2**31)
