# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        sortednums=[]
        def self(node):
            if node.left:
                self(node.left)
            sortednums.append(node.val)
            if node.right:
                self(node.right)
            return node
        self(root)
        return sortednums[k-1]