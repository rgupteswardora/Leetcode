class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        lis=[[1]]
        for i in range(numRows-1):
            tem=[0]+lis[-1]+[0]
            rw=[]
            for j in range(len(lis[-1])+1):
                rw.append(tem[j]+tem[j+1])
            lis.append(rw)
            rw=[]
        return lis