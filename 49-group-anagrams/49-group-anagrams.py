class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dis=collections.defaultdict(list)
        
        for st in strs:
            coutn=[0]*26
            
            for c in st:
                coutn[ord(c)-ord("a")]+=1
            
            dis[tuple(coutn)].append(st)
        return dis.values()
        