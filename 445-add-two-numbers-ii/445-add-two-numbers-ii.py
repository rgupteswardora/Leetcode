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
        node1=l1
        node2=l2
        num1="" #number2
        num2="" #number2
        sumnum=[]
        rem=0
        while node1:
            num1=num1+str(node1.val)
            node1=node1.next
        while node2:
            num2=num2+str(node2.val)
            node2=node2.next
        #7243
        # 564
        mi=(max(len(num1),len(num2)))-(min(len(num1),len(num2)))
        print(num1,num2,mi)
        j=min(int(num1),int(num2))
        j=str(j)
        sj=(mi*'0')+str(min(int(num1),int(num2)))
        print(j)
        if(j==num2):
            num2=sj
        else:
            num1=sj
        sum=int(num1)+int(num2)
        sumnum=list(str(sum))
        dummy1,dummy2=ListNode(),ListNode()
        dummy1.next=dummy2
        for i in sumnum:
            dummy2.next=ListNode(int(i))
            dummy2=dummy2.next
        return dummy1.next.next