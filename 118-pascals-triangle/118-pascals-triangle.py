class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output=[[1]]
        for i in range(numRows-1):
            temp=[0]+output[-1]+[0]
            rw=[]
            for j in range(len(output[-1])+1):
                rw.append(temp[j]+temp[j+1])
            output.append(rw)
            rw=[]
        return output