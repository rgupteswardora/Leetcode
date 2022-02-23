# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def check(node,val):
            sum=0
            if not node:
                return 0
            if not node.left and not node.right:
                if val==1:
                    print(node.val)
                    sum=sum+node.val
            sum=sum+check(node.left,1)
            sum=sum+check(node.right,2)
            return sum
        return (check(root,0))