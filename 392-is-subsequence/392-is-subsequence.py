class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i,j=0,0
        le=len(s)
        while j<len(t) and i<len(s):
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i==le:
            return True
        return False