# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def rec(arr):
            if not arr:
                return None
            mid = 0 + (len(arr)-1 - 0)//2
            node = TreeNode(arr[mid])
            node.left = rec(arr[:mid])
            node.right = rec(arr[mid+1:])
            return node
        return rec(nums)