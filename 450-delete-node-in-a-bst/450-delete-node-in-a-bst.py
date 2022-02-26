# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def findmin(node):
            current=node
            while current.left:
                current=current.left
            return current
        if not root:
            return root
        elif key < root.val:
            root.left=self.deleteNode(root.left,key)
        elif key > root.val:
            root.right=self.deleteNode(root.right,key)
        else:
            if root.left==None and root.right==None:
                root=None
            elif root.left==None:
                root=root.right
            elif root.right==None:
                root=root.left
            else:
                Minimum=findmin(root.right)
                root.val=Minimum.val
                root.right=self.deleteNode(root.right,Minimum.val)
        return root
                