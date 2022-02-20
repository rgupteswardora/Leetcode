class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        last=len(digits)-1
        ret=digits
        ret[last]=ret[last]+1
        for i in range(last,-1,-1):
            if(ret[i]>=10):
                if(i!=0):
                    j=ret[i]//10
                    ret[i]=ret[i]%10
                    ret[i-1]=ret[i-1]+j
                elif(i==0):
                    a=[]
                    j=ret[i]//10
                    ret[i]=ret[i]%10
                    a.append(j)
                    a.extend(ret)
                    ret=a
        return ret