class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[]
        count=0
        for ch in s:
            if ch=='(':
                l.append(count)
                count=0
            elif ch==")":
                count=l.pop()+max(count*2,1)
        return count
        