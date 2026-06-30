# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: 
            return []

        q = deque([root])
        res = [[]]
        index = 0

        while q: 
            length = len(q)

            for _ in range(length):

                current = q.popleft()
                res[index].append(current.val)

                if current.left: 
                    q.append(current.left)
                
                if current.right: 
                    q.append(current.right)

            res.append([])
            index += 1
        
        res.pop()

        return res