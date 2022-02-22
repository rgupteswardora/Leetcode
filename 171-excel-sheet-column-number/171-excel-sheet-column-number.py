class Solution(object):
    def titleToNumber(self, st):
        """
        :type columnTitle: str
        :rtype: int
        """
        sum=0
        st=st[::-1]
        for s in range(0,len(st)):
            if s==0:
                sum=sum+(ord(st[s])-64)
            else:
                sum=sum+26**s*(ord(st[s])-64)
        return sum