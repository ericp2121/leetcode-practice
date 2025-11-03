# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        def explore(node, node2):
            

            if not node and not node2:
                return True
                # reached end of tree, and no error that forced quit before, so end
            elif not node or not node2:
                return False
                # error case that one child is missing when other has child, so end with false
            elif node.val != node2.val:
                return False
                # error case that value not equal, so end with false

            return explore(node.left, node2.left) and explore(node.right, node2.right)
            # return combined result of checking BOTH left child and BOTH right children at same time



        return explore(p,q)
    

    '''

    # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        def explore(node, node2, check):
            

            if not node and not node2:
                return True
            elif not node or not node2:
                return False
            elif node.val != node2.val:
                return False

            
            if (node.left and node2.left) and (node.left.val == node2.left.val):
                explore(node.left, node2.left, True)
            else:
                return False




            if (node.right and node2.right) and (node.right.val == node2.right.val):
                explore(node.right, node2.right, True)
            else:
                return False
            

            return True
            
           

        return explore(p,q,True)


    #### unfortunately, this code is unable to handle no children edge case ####
    '''