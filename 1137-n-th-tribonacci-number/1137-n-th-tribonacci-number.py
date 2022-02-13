class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        one,two,three=0,1,1
        if(n==0):
            return 0
        if(n==1):
            return 1
        elif(n==2):
            return 1
        else:
            for i in range(0,n-2):
                temp1=two
                temp2=three
                three=one+two+three
                one=temp1
                two=temp2
        return three