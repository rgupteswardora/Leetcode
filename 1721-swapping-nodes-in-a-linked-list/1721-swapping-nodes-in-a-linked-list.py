# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy1,dummy2=ListNode(),ListNode()
        dummy1.next=dummy2
        lis=[]
        node=head
        while node:
            lis.append(node.val)
            node=node.next
        lis[k-1],lis[-k]=lis[-k],lis[k-1]
        for i in lis:
            node=ListNode(i)
            dummy2.next=node
            dummy2=dummy2.next
        return dummy1.next.next
        