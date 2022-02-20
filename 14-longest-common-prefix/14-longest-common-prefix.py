class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        returnst=""
        res = min(strs, key = len) 
        for i in range(0,len(res)):
            for strings in strs:
                if strings[i]!=res[i]:
                    return returnst
            returnst+=res[i]
        return returnst