"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        copynode={None:None}
        cur=head
        while cur:
            node=Node(cur.val)
            copynode[cur]=node
            cur=cur.next
        cur=head
        while cur:
            copy=copynode[cur]
            copy.next=copynode[cur.next]
            copy.random=copynode[cur.random]
            cur=cur.next
        return copynode[head]