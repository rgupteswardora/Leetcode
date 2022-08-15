class Solution:
    def countSubstrings(self, s: str) -> int:
        ha={}
        for i in range(0,len(s)):
            st=""
            for j in range(i,len(s)):
                st=st+s[j]
                if(st==st[::-1]):
                    if(st not in ha):
                        ha[st]=1
                    else:
                        ha[st]=ha[st]+1
        return sum(ha.values())
        