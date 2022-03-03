# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lis=[]
        def self(node):
            if node:
                if node.left:
                    self(node.left)
                if node.right:
                    self(node.right)
                
                lis.append(node.val)
        self(root)
        return lis