class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maximumArea = 0

        while left < right:
            totalArea = min(heights[left], heights[right]) * (right - left)
            maximumArea = max(maximumArea, totalArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maximumArea