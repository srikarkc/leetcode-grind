class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        counter = 0

        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    counter += 1
            elif i == len(flowerbed) -1:
                if flowerbed[-2] == 0 and flowerbed[-1] == 0:
                    counter += 1
            else:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    counter += 1
            
        if counter >= n:
            return True
        else:
            return False
    
flowerbed = [1,0,0,0,1], n = 1