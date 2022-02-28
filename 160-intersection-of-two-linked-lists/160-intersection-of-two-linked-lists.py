# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nod1=headA
        nod2=headB
        len1,len2=0,0
        while nod1:
            len1+=1
            nod1=nod1.next
        while nod2:
            len2+=1
            nod2=nod2.next
        mov=abs(len1-len2)
        nod1=headA
        nod2=headB
        if len1>len2:
            while mov!=0:
                nod1=nod1.next
                mov-=1
        elif len1<len2:
            while mov!=0:
                nod2=nod2.next
                mov-=1
        while nod1 and nod2:
            if nod1==nod2:
                return nod1
            nod1=nod1.next
            nod2=nod2.next
        return None
            