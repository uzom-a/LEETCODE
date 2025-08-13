# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []  #since this is defined outside the inner function no need to call it in the inner function
        def dfs(node):
            if not node:
                return []
                
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

            return result

        return dfs(root)


# Time Complexity: O(n)
# Space Complexity: O(n)