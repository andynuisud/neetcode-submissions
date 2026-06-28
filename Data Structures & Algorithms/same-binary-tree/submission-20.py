# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        """
            Use dfs to check if the node is the same. 
            Now problem is split into two parts. Check right and left tree

            Create a recursive function, first check if head is the same
            Compare with the rest of the tree
        """

        def dfs(node1, node2):

            #Check if the head node is the same

            if not node1 and not node2: 
                return True 

            if not node1 or not node2: 
                return False 

            if node1.val != node2.val: 
                return False

            #Check the left and right tree
            leftTree = dfs(node1.left, node2.left)
            rightTree = dfs(node1.right, node2.right)

            if leftTree and rightTree: 
                return True 
            else: 
                return False 

        res = dfs(p, q)
        return res 