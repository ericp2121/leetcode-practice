# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]

        Inorder traversal: left subtree → root → right subtree

        Key concepts:

        1. Recursion:
           - Each node is treated as the root of its own subtree.
           - The same function is applied to smaller subtrees.
           - The recursion stack automatically remembers the parent nodes.
        
        2. Traversal steps for any node:
           a) Explore left subtree completely (go left until no child)
           b) Record the current node (after left subtree)
           c) Explore right subtree completely

        3. Why no else is needed:
           - traversal.append(node.val) happens **after left recursion returns**
             for every node.
           - For leftmost nodes, left child is None → append executes immediately.
           - For nodes with left children, recursion returns after exploring left subtree,
             then append executes automatically.
        
        4. How parent nodes are revisited:
           - When a recursive call finishes, control returns to the previous call,
             which still has 'node' pointing to the parent.
           - This is why we automatically move back to root to then explore right subtree.
        """

        traversal = []

        def explore(node):
            if not node:
                return  # base case: nothing to do if node is None
                # this will exit the current child checker if there is no node, ie no left/right child
                # then return to the previous value, where it is then recorded 

            # 1️⃣ traverse left subtree
            if node.left:
                explore(node.left)
                # Recursion goes all the way to the leftmost node.
                # Leftmost node has no left child → base case triggers
                # After returning from leftmost node, we continue at current node

            # 2️⃣ record current node
            print("Visiting:", node.val)  # optional: see traversal order
            traversal.append(node.val)
            # Recording happens **after left subtree is fully explored**
            # This ensures left → root order
            # is always safe without else, is that the return function above will execute first always , 
            # so it will not reach this code if the previous if statement fails to find a child

            # it is after explore left because you always want left most node 

            # 3️⃣ traverse right subtree
            if node.right:
                explore(node.right)
                # Recursion now handles the right subtree
                # Each right child becomes a new "current node" and repeats left→root→right

                # keep checking right until left fails, it will always record the left node. 

        # Start recursion at root
        explore(root)
        return traversal
