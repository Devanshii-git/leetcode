class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        area=0
        while left<right:
            width=right-left
            hite=min(height[left],height[right])
            area=max(area,width*hite)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area