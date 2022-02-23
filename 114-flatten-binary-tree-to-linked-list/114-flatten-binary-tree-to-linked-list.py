# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        lis=[]
        def self(node):
            if node:
                lis.append(node.val)
                if node.left:
                    self(node.left)
                if node.right:
                    self(node.right)
        self(root)
        print(lis)
        if root:
            root.left=None
            for i in lis[1:]:
                test=TreeNode(i)
                root.right=test
                root=root.right