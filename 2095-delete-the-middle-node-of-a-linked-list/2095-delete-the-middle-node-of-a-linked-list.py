# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        len=0
        node1=head
        while node1:
            len+=1
            node1=node1.next
        if len==1:
            return node1
        delnode=len//2
        i=0
        print(i,delnode)
        dummy=ListNode(0,head)
        node1=head
        while node1:
            if(i==delnode):
                dummy.next=dummy.next.next
            node1=node1.next
            dummy=dummy.next
            i+=1
        return head