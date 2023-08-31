# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        if root:
            q = [root]
            while len(q) > 0:
                level = []
                for i in range(len(q)):
                    temp = q.pop(0)
                    level.append(temp.val)
                    if temp.left:
                        q.append(temp.left)

                    if temp.right:
                        q.append(temp.right)
                        
                arr.append(level)

        return arr