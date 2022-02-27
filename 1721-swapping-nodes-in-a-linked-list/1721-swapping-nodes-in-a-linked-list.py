# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        lis=[]
        node=head
        while node:
            lis.append(node.val)
            node=node.next
        lis[k-1],lis[-k]=lis[-k],lis[k-1]
        dummy1,dummy2=ListNode(),ListNode()
        dummy1.next=dummy2
        for i in lis:
            nd=ListNode(i)
            dummy2.next=nd
            dummy2=dummy2.next
        return dummy1.next.next