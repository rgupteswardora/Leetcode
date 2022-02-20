class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        box={}
        num=0
        sum=0
        for i in range(lowLimit,highLimit+1):
            num=i
            while(num!=0):
                sum=sum+(num%10)
                num=num//10
            if sum in box:
                box[sum]+=1
            else:
                box[sum]=1
            sum=0
        return (max(box.values()))