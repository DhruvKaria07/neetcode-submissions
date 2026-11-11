class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        runningProduct = 1
        for i in range(len(nums)):
            left[i] = runningProduct
            runningProduct *= nums[i]
        
        runningProduct = 1
        for i in range(len(nums) -1, -1, -1):
            left[i] *= runningProduct
            runningProduct *= nums[i]

        return left