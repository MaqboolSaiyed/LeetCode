# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def checkBalance(node):
            if not node:
                return 0, True
            leftHeight, leftBalanced = checkBalance(node.left)
            rightHeight, rightBalanced = checkBalance(node.right)
            return max(leftHeight, rightHeight) + 1, leftBalanced and rightBalanced and abs(leftHeight - rightHeight) <= 1
        
        return checkBalance(root)[1]