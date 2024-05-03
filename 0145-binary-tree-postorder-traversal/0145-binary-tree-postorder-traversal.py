class Solution:
    def postorderTraversal(self, root):
        result = []

        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                result.append(node.val)

        postorder(root)
        return result