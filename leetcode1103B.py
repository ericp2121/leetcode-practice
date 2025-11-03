# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        depth = 0
        
        def explore(node, depth):
            if not node:
                return depth
            
            Leftdepth = depth
            rightdepth = depth

            if node.left:
                # capture the return value of recursion
                Leftdepth = explore(node.left, depth + 1)

            if node.right:
                # capture the return value of recursion
                rightdepth = explore(node.right, depth + 1)

            return max(Leftdepth, rightdepth)

        if not root:
            return 0
        else:
            return explore(root, depth) + 1
