# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        carry = False
        first = second = 0
        solution = curr = ListNode(None, None)
        while l1 or l2:
            newVal = 0
            if carry: newVal = 1
            if l1: newVal+= l1.val
            if l2: newVal+= l2.val
            if newVal>9: carry = True
            else: carry = False
            curr.next = ListNode(newVal%10)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry:
            curr.next = ListNode(1)
        return solution.next