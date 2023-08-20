# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root, subRoot) -> bool:
    if root and subRoot:
        if root.val == subRoot.val:
            return isSubtree(root.right, subRoot.right) and isSubtree(root.left, subRoot.left)
        else:
            return isSubtree(root.right, subRoot) and isSubtree(root.left, subRoot)
    elif root == None and subRoot == None:
        return True
    else:
        return False

root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))

print(isSubtree(root, subRoot))