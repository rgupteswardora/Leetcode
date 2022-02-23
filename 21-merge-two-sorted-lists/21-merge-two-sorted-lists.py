# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy1,dummy2=ListNode(),ListNode()
        dummy1.next=dummy2
        lis1=[]
        def ele(node):
            while node:
                lis1.append(node.val)
                node=node.next
        ele(list1)
        ele(list2)
        lis1.sort()
        for i in lis1:
            node=ListNode(i)
            dummy2.next=node
            dummy2=dummy2.next
        return dummy1.next.next