"""
https://leetcode.com/problems/add-two-numbers/#/description
status: done
topics: LINKED LISTS
difficulty: medium

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of the nodes contains a single
digit. Add the two numbers and return it as a linked list. Assume the numbers
don't contain any leading zeros, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8


Algorithm (from leetcode.com, implemented by me in Python):
Initialize first node (or empty dummy node) of return list.
Initialize a variable for carry value.
Initialize variables to heads of l1 and l2.
Iterate over l1 and l2 until you reach the end.
    Get l1 value
    Get l2 value
    Set sum variable
    Update carry value
    Create new node with value of sum
    Advance over l1 and l2
Once at the end, check if carry value is 1, if so append accordingly
Return head of return list

"""

class ListNode(object):
    def __init__(self, digit, next):
        self.val = digit
        self.next = next

def add_two_numbers(l1, l2):
    dummy_head = ListNode(0, None)
    curr = dummy_head
    carry_digit = 0 # will always be 0 or 1 (since we're only adding two nums, max sum is 18)

    l1node = l1
    l2node = l2

    while l1node is not None or l2node is not None:
        if l1node is not None:
            l1val = l1node.val
        else:
            l1val = 0
        if l2node is not None:
            l2val = l2node.val
        else:
            l2val = 0
        # print "l1val: %d, l2val: %d " % (l1val, l2val)
        
        sum_val = l1val + l2val + carry_digit
        # print "existing carry: %d" % carry_digit
        # print "sum: %d" % sum_val
        
        carry_digit = sum_val / 10
        # print "new carry: %d" % carry_digit
        
        new_node_val = sum_val % 10
        # print "new node: %d" % new_node_val
        curr.next = ListNode(new_node_val, None)
        curr = curr.next
        if l1node is not None:
            l1node = l1node.next
        if l2node is not None:
            l2node = l2node.next
    if carry_digit > 0:
        # print "remaining carry: %d" % carry_digit
        curr.next = ListNode(carry_digit, None)
    
    check = dummy_head.next
    while check is not None:
        check = check.next
    
    return dummy_head.next


####################
# TESTING

# First number is abc - 342
# Second number is def - 465
# Sum is 807

# 123 + 456 = 579
# 89 + 234 = 323
# 9876 + 765 = 10641

a = ListNode(9, None)
b = ListNode(8, a)
c = ListNode(7, b)
d = ListNode(6, c)

e = ListNode(7, None)
f = ListNode(6, e)
g = ListNode(5, f)

# 19 + 23 = 42
# a = ListNode(1, None)
# b = ListNode(9, a)

# c = ListNode(2, None)
# d = ListNode(3, c)

print add_two_numbers(d, g)
