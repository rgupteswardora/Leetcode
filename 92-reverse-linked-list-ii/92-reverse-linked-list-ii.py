# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy1,dummy2=ListNode(),ListNode()
        dummy1.next=dummy2
        lis=[]
        node=head
        while node:
            lis.append(node.val)
            node=node.next
        dummylis=lis[left-1:right]
        rtlis=lis[0:left-1]+dummylis[::-1]+lis[right:]
        for i in rtlis:
            nd=ListNode(i)
            dummy2.next=nd
            dummy2=dummy2.next
        return dummy1.next.next