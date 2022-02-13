class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        num=0
        le=list(s)
        while(len(le)!=0):
            st=le.pop(0)
            if(len(le)!=0 and val[st]<val[le[0]]):
                num=num+(val[le[0]]-val[st])
                le.pop(0)
            else:
                num=num+val[st]
        return num