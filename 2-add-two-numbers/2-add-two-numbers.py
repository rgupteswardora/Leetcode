# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        tail=dummy
        num1=""
        num2=""
        node1=l1
        node2=l2
        while(node1):
            num1=num1+str(node1.val)
            node1=node1.next
        while(node2):
            num2=num2+str(+node2.val)
            node2=node2.next
        rem=0
        sumofnum=""
        rem=0
        temp=0
        stnum1=str(num1)
        stnum2=str(num2)
        maxlen=max(len(stnum1),len(stnum2))
        for i in range(0,maxlen):
            if(i<len(stnum1) and i<len(stnum2)):
                 temp=rem+int(stnum1[i])+int(stnum2[i])
                 rem=0
            if(i>=len(stnum1)):
                 temp=rem+int(stnum2[i])
                 rem=0
            if(i>=len(stnum2)):
                 temp=rem+int(stnum1[i])
                 rem=0
            if(temp>=10):
                rem=1
                sumofnum=str(sumofnum+str(temp)[1])
            else:
                sumofnum=sumofnum+(str(temp))
        if(rem==1):
            sumofnum=sumofnum+str(1)
        for s in sumofnum:
            new_node=ListNode(s)
            tail.next=new_node
            tail=tail.next
        return dummy.next
        