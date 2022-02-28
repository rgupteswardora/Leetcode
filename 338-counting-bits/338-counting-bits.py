class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        rt=[]
        for i in range(0,n+1):
            r=bin(i).replace("0b", "")
            ct=counter = r.count('1')
            rt.append(ct)
        return rt