class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        one,two=1,1
        if(n==0):
            return 0
        elif(n==1):
            return 1
        elif(n==2):
            return 1
        else:
            for i in range(0,n-2):
                temp=one
                one=one+two
                two=temp
        return one