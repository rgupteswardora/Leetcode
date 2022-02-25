class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        lis1=version1.split(".")
        lis2=version2.split(".")
        num1,num2=[],[]
        for i in lis1:
            num1.append(int(i))
        for j in lis2:
            num2.append(int(j))
        if len(num1)>len(num2):
            for i in range(len(num1)-len(num2)):
                num2.append(0)
        if len(num1)<len(num2):
            for i in range(len(num2)-len(num1)):
                num1.append(0)
        print(num1,num2)
        for i in range(len(num1)):
            if num1[i]>num2[i]:
                return 1
            elif num1[i]<num2[i]:
                return -1
        return 0