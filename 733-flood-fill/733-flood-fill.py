class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows,columns=len(image)-1,len(image[0])-1
        def serch(image, sr, sc, newColor):
            if(image[sr][sc]!=newColor):
                temp=image[sr][sc]
                image[sr][sc]=newColor
                if rows>=(sr-1)>=0 and columns>=sc>=0:                   #up
                    if(temp==image[sr-1][sc]):
                        serch(image,sr-1,sc,newColor)
                if rows>=(sr)>=0 and columns>=sc-1>=0:                   #right
                    if(temp==image[sr][sc-1]):
                        serch(image,sr,sc-1,newColor)
                if rows>=(sr)>=0 and columns>=sc+1>=0:                   #up
                    if(temp==image[sr][sc+1]):
                        serch(image,sr,sc+1,newColor)
                if rows>=(sr+1)>=0 and columns>=sc>=0:                   #up
                    if(temp==image[sr+1][sc]):
                        serch(image,sr+1,sc,newColor)
                return image
        serch(image, sr, sc, newColor)
        return image