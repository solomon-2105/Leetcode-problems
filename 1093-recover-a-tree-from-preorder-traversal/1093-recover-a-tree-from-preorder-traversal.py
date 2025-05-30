# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: TreeNode
        """
        stack = []  # stack of (node, depth)
        i = 0
        n = len(traversal)

        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1

            value = 0
            while i < n and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1

            node = TreeNode(value)

            while stack and stack[-1][1] >= depth:
                stack.pop()

            if stack:
                parent = stack[-1][0]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

            stack.append((node, depth))

        return stack[0][0] if stack else None
