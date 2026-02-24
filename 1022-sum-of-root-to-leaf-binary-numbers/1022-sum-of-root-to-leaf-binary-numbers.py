# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
#         paths = self.collect_paths(root)
#         total = 0
#         for p in paths:
#             total += int(p, 2)  
#         return total

#     def collect_paths(self, root):
#         res = []
#         def dfs(node, path):
#             if not node:
#                 return
#             path.append(str(node.val))
#             if not node.left and not node.right:
#                 res.append("".join(path))
#             else:
#                 dfs(node.left, path)
#                 dfs(node.right, path)
#             path.pop()
#         dfs(root, [])
#         return res

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current):
            if not node:
                return 0
            current = current * 2 + node.val
            if not node.left and not node.right:
                return current
            return dfs(node.left, current) + dfs(node.right, current)
        return dfs(root, 0)