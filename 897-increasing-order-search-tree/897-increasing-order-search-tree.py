# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        dummy1,dummy2=TreeNode(),TreeNode()
        dummy1.right=dummy2
        lis=[]
        def self(node):
            if node.left:
                self(node.left)
            lis.append(node.val)
            if node.right:
                self(node.right)
            return node
        self(root)
        print(lis)
        for i in lis:
            dumdum=TreeNode(i)
            dummy2.right=dumdum
            dummy2=dummy2.right
        return dummy1.right.right
                