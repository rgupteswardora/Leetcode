# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left,right=ListNode(),ListNode()
        ptrleft,ptrright=left,right
        node1=head
        while node1:
            if(node1.val<x):
                ptrleft.next=ListNode(node1.val)
                ptrleft=ptrleft.next
            else:
                ptrright.next=ListNode(node1.val)
                ptrright=ptrright.next
            node1=node1.next
        ptrleft.next=right.next
        ptrright.next=None
        return left.next