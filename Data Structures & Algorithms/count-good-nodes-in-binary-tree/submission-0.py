# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.counter = 0
        

        def dfs(node, previousMax):

            if not node: 
                return None

            if (node.val >= previousMax): 
                self.counter += 1
                previousMax = node.val
            
            print(previousMax)

            if node.left: 
                dfs(node.left, previousMax)

            if node.right: 
                dfs(node.right, previousMax)


        dfs(root, root.val)
        return self.counter