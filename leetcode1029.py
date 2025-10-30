# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def explore(node,sum):
            
            if not node:
                return False
                # quit if no more child nodes

            new_sum = sum + node.val
            # checking sum at every child
            # no need to specify this at left/right explore because explore calls entire func anyways
            # if calculate in left/right, will calculate nodes twice (ie recursed into function , recalculated within left explore)
            # ie, if left and right children exist it will mix them into this
            if node.left is None and node.right is None and new_sum == targetSum:
                return True
                # ONLY case to return true; ie , no mode child and the sum is equal to target Sum

            if node.left:
                print('sum currently is ',new_sum)
                if explore(node.left, new_sum):
                    return True
                    # return True otherwise it will by default return null

           
            if node.right:
                # new_sum = sum + node.val
                print('sum currently is ',new_sum)
                if explore(node.right, new_sum):
                    return True
                
            '''
            Each recursive call assumes optimistically that a valid path might exist through its children.

            If a child finds the target sum, it returns True immediately, which propagates all the way back up the call stack—each parent 
            call just passes that True upward.

            If no child ever finds the target sum, then nothing returns True, so eventually the recursion hits the bottom and False 
            cascades back up to the top.
            '''

        
            return False



        result = explore(root,0)
        return result
        # return False
        