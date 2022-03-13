class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        li=[]
        l=[]
        for i in s:
            l.append(i)
            if i=="(" or i=='[' or i=="{":
                li.append(i)
            if len(li)==0:
                return False
            if i=="]" and li[-1]=="[":
                l.remove(']')
                l.remove('[')
                li.pop()
            if i==")" and li[-1]=="(":
                l.remove('(')
                l.remove(')')
                li.pop()
            if i=="}" and li[-1]=="{":
                l.remove('{')
                l.remove('}')
                li.pop()
        if len(li)==0 and len(l)==0:
            return True
        return False
            
                