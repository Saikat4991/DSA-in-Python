# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True, 0 #balanced and height = 0

            left_balanced, left_height = dfs(root.left)
            right_balanced, right_height = dfs(root.right)

            current_balanced = left_balanced and right_balanced and abs(left_height - right_height)<= 1
            current_height = 1 + max(left_height, right_height)

            return current_balanced, current_height

        
        return dfs(root)[0]

            

        