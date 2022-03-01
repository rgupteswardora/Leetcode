# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr=[]
        node=head
        while node:
            arr.append(node.val)
            node=node.next
        arr.sort()
        dummy1,dummy2=ListNode(),ListNode()
        dummy1.next=dummy2
        for i in arr:
            nod=ListNode(i)
            dummy2.next=nod
            dummy2=dummy2.next
        return dummy1.next.next