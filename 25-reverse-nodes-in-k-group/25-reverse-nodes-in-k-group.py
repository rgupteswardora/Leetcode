# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy1,dummy2=ListNode(),ListNode()
        dummy1.next=dummy2
        lis=[]
        dumlis=[]
        node=head
        count=0
        while node:
            count+=1
            dumlis.append(node.val)
            node=node.next
            if count==k:
                lis=lis+dumlis[::-1]
                dumlis=[]
                count=0
        lis=lis+dumlis
        for i in lis:
            nd=ListNode(i)
            dummy2.next=nd
            dummy2=dummy2.next
        return dummy1.next.next        