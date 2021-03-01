# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        view = [[]]
        def rec(node, level):
            nonlocal view
            if not node:
                return
            if level == len(view):
                view.append([])
            view[level-1].append(node.val)
            rec(node.left, level+1)
            rec(node.right, level+1)
            return
        rec(root,1)
        sol = []
        for x in view:
            if x:
                sol.append(x[-1])
        return sol