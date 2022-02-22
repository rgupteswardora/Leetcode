# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, node, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if val == node.val:
            print(node.val)
            return node
        elif val < node.val:
            if node.left:
                return self.searchBST(node.left,val)
        elif val > node.val:
            if node.right:
                return self.searchBST(node.right,val)