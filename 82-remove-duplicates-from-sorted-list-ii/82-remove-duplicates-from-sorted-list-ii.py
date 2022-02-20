# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0,head)
        prev=dummy
        check=head
        while check:
            if(check.next and check.val==check.next.val):
                while(check.next and check.val==check.next.val):
                    check=check.next
                prev.next=check.next
            else:
                prev=prev.next
            check=check.next
        return dummy.next
        