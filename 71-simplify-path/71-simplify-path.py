class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        li=[]
        cur=""
        for c in path+"/":
            if c=='/':
                if cur=="..":
                    if li: li.pop()
                elif cur!="" and cur!=".":
                    li.append(cur)
                cur=""
            else:
                cur+=c
        return ("/"+"/".join(li))