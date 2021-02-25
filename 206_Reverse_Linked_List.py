# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = None
        def reverse(node1, node2):
            if not node2:
                return node1
            _next = node2.next
            node2.next = node1
            return reverse(node2, _next)
        return reverse(dummy, head)