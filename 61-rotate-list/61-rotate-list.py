# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        lis=[]
        newlis=[]
        node1=head
        while node1:
            lis.append(node1.val)
            node1=node1.next
        if(len(lis)==1 or len(lis)==0):
            node1=head
            return node1
        if(len(lis)<k):
            if(k%len(lis)==0):
                k=len(lis)
            else:
                k=(k%len(lis))
        for i in range(k):
            newlis.append(lis[-1])
            newlis.extend(lis[0:len(lis)-1])
            lis=newlis
            newlis=[]
        dummy1=ListNode(0)
        dummy=ListNode(0)
        dummy1.next=dummy
        for i in lis:
            dummy.next=ListNode(i)
            dummy=dummy.next
        return dummy1.next.next