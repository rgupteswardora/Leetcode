# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        st=""
        node=head
        while node:
            st=st+str(node.val)
            node=node.next
        if st==st[::-1]: return True
        return False