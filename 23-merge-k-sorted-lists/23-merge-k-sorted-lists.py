# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy1,dummy2=ListNode(),ListNode()
        dummy1.next=dummy2
        lis=[]
        for i in lists:
            nd=i
            while nd:
                lis.append(nd.val)
                nd=nd.next
        lis.sort()
        for i in lis:
            node=ListNode(i)
            dummy2.next=node
            dummy2=dummy2.next
        return dummy1.next.next