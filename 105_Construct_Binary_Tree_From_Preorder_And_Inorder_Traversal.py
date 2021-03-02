import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = collections.deque(preorder)
        def rec(arr):
            if not arr or not preorder:
                return None
            curr = preorder.popleft()
            root = TreeNode(curr)
            ind = arr.index(curr)
            root.left = rec(arr[:ind])
            root.right = rec(arr[ind+1:])
            return root
        return rec(inorder)