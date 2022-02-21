# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummynode=ListNode()
        dummynode2=ListNode()
        odd,even=ListNode(),ListNode()
        dummynode.next=odd
        dummynode2.next=even
        count=0
        node1=head
        while node1:
            count+=1
            if(count%2==0):
                node=ListNode(node1.val)
                even.next=node
                even=even.next
            else:
                node=ListNode(node1.val)
                odd.next=node
                odd=odd.next
            node1=node1.next
        odd.next=dummynode2.next.next
        return dummynode.next.next