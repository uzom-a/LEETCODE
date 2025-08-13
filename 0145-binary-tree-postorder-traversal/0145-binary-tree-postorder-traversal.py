# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node, result):
            if not node:
                return []

            dfs(node.left, result)
            dfs(node.right, result)
            result.append(node.val)

            return result
        return dfs(root, result)

    # Space Complexity = O(n)
    # Time Complexity = O(n)