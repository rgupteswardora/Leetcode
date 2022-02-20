class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        st="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        allst=set(st)
        allsub=[]
        st=""
        for i in range(0,len(s)):
            if s[i] in allst:
                st=st+s[i]
            elif(len(st)!=0):
                allsub.append(st)
                st=""
        if(len(st)!=0):
                allsub.append(st)
                st=""
        return len(allsub[-1])