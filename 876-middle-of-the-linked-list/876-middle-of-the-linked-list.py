# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        len=0
        node1=head
        while node1:
            len=len+1
            node1=node1.next
        node1=head
        mid=len/2
        start=0
        while(start!=mid):
            node1=node1.next
            start+=1
        return node1