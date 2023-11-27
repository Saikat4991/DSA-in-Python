# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0 #initialize max diameter = 0

        def dfs(root):
            nonlocal maxD #nonlocalize maxD, allowing it to modify from outer function

            # If the current node (root) is None, the function returns 0. This is the base case for the recursion.
            if not root:
                return 0

            #recursive calls
            left = dfs(root.left)
            right = dfs(root.right)

            maxD = max(maxD, left+right)

            return 1+max(left,right)

        dfs(root)
        return maxD

            

        