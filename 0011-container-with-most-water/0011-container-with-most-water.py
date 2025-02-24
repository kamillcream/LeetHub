class Solution(object):
    def maxArea(self, height):
        
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            water = (right - left) * min(height[left], height[right])
            max_water = max(max_water, water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water   

            
            
        