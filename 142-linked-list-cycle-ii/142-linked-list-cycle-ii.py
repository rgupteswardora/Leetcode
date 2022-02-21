# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hashset={}
        count=0
        node1=head
        while node1:
            if id(node1) not in hashset:
                hashset[id(node1)]=count
                count+=1
            else:
                return node1
            node1=node1.next