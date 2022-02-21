# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        lis=[]
        node1=head
        while node1:
            lis.append(node1.val)
            node1=node1.next
        newlis=[]
        n=len(lis)
        i=0
        while(len(newlis)!=n):
            newlis.append(lis[i])
            if(len(newlis)!=n):
                newlis.append(lis[n-1-i])
            i=i+1
        node1=head
        i=0
        while node1:
            node1.val=newlis[i]
            node1=node1.next
            i+=1