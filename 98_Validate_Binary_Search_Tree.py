# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        def rec(node, _min, _max):
            if not node:
                return True
            return _min<node.val<_max and rec(node.left, _min, node.val) and rec(node.right, node.val, _max)
            
        return rec(root, float('-inf'), float('inf'))