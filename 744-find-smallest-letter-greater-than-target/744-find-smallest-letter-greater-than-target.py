class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        low,high=0,len(letters)
        while(low<high):
            mid=(low+high)//2
            if(letters[mid]<=target):
                low=mid+1
            else:
                high=mid
        return letters[low % len(letters)]