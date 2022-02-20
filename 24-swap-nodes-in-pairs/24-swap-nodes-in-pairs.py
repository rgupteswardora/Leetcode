# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dumm1=ListNode(0,None)
        dummy=ListNode(0,None)
        dumm1.next=dummy
        node1=head
        len=0
        while node1:
            len+=1
            node1=node1.next
        node1=head
        if(len==1):
            return node1
        elif(len%2==0 or len==0):
            while node1 and node1.next:
                a=node1.val
                b=node1.next.val
                dummy.next=ListNode(b)
                dummy=dummy.next
                dummy.next=ListNode(a)
                dummy=dummy.next
                node1=node1.next.next
            return dumm1.next.next
        else:
            while node1 and node1.next:
                a=node1.val
                b=node1.next.val
                dummy.next=ListNode(b)
                dummy=dummy.next
                dummy.next=ListNode(a)
                dummy=dummy.next
                node1=node1.next.next
            dummy.next=ListNode(node1.val)
            dummy=dummy.next
            return dumm1.next.next