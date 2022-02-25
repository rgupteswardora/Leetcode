class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            res=helper(x,n//2)
            if n%2==0:
                return res*res
            else:
                return x*res*res
        if x==0:
                return 0
        if n==0:
                return 1
        if n>0:
            return helper(x,n)
        else:
            return 1/helper(x,-1*n)