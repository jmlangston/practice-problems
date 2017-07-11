"""
https://leetcode.com/problems/two-sum/#/description
topics: PYTHON DICTIONARY (HASH TABLE)
difficulty: easy

Given an array of integers, return indices of the two numbers such that they add
up to a specific target. Assume each input would have exactly one solution, and
you may not use the same element twice.

Example:
    nums = [2, 7, 11, 15]
    target = 9

    Return [0, 1] because nums[0] + nums[1] = 9

Example (where two nums are the same):
    nums = [1, 2, 4, 5, 4]
    target = 8

    Return [2, 4]

"""

# my solution
def two_sum(nums, target):
    # start looking for match by iterating over list of numbers
    for num in nums:
        diff = target - num
        if diff in nums:

            # special case - two occurences of number and they add up to target
            # ex: 4 and 4 are in the list and 8 is the target
            if diff == num and nums.count(num) > 1:
                # find the index of the second occurrence
                ind_num = nums.index(num)
                # look for second occurrence starting with next num in nums
                i = ind_num + 1
                ind_diff = None
                while i < len(nums) and ind_diff is None:
                    if nums[i] == num:
                        ind_diff = i
                    else:
                        i += 1

            # all other cases jump straight to...
            else:
                ind_num = nums.index(num)
                ind_diff = nums.index(diff)

            return [ind_num, ind_diff]


# nums = [2, 7, 11, 15]
# target = 9

# nums = [1, 2, 4, 5, 4, 7, 7, 5]
# target = 10

# nums = [0, -5, 6, 8, 13]
# target = 1

# nums = [3, 2, 4]
# target = 6

print two_sum(nums, target)


##############################
# SOLUTIONS from leetcode.com

def soln_one(nums, target):
    # O(n^2) runtime and O(1) space complexity
    i = 0
    j = 1
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

# print soln_one(nums, target)


def soln_two(nums, target):
    # O(n) runtime and O(n) space complexity
    # uses HASH TABLE, i.e. Python dictionary

    nums_dict = {}

    for i in range (0, len(nums)):
        nums_dict[nums[i]] = i

    for i in range(0, len(nums)):
        diff = target - nums[i]
        if diff in nums_dict and nums_dict[diff] != i:
            return [i, nums_dict[diff]]

# print soln_two(nums, target)


def soln_three(nums, target):
    # O(n) runtime and O(n) space complexity
    # HASH TABLE with only one pass (other solution uses two passes)

    nums_dict = {}

    for i in range(0, len(nums)):
        diff = target - nums[i]
        if diff in nums_dict:
            return [nums_dict[diff], i]
        nums_dict[nums[i]] = i

# print soln_three(nums, target)
