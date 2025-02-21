class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                prev_empty = (i == 0) or (flowerbed[i-1] == 0) # 첫번째 자리거나 왼쪽이 0인지
                next_empty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0) # 마지막 자리거나 오른쪽이 0인지

                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0: # 필요한 만큼 심었으면 종료
                        return True
            
        return False
            
        