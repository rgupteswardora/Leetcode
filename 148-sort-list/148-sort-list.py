# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy1=ListNode()
        dummy2=ListNode()
        dummy1.next=dummy2
        lis=[]
        node1=head
        while node1:
            lis.append(node1.val)
            node1=node1.next
        lis.sort()
        for i in lis:
            node=ListNode(i)
            dummy2.next=node
            dummy2=dummy2.next
        return dummy1.next.next