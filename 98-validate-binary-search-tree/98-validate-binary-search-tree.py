# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        lis=[]
        def self(node):
            if node.left:
                self(node.left)
            lis.append(node.val)
            if node.right:
                self(node.right)
            return node
        self(root)
        check=list(set(lis[:]))
        check.sort()
        if check==lis:
            return True
        return False