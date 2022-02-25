class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        num=0
        i=0
        lastindex=len(s)-1
        while(i<lastindex):
            if(val[s[i+1]]>val[s[i]]):
                num=num+val[s[i+1]]-val[s[i]]
                i+=2
            else:
                num=num+val[s[i]]
                i+=1
        if i==lastindex:
            num=num+val[s[i]]
        return num