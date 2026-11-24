class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfyt = 0
        for x in prices:
            if x < minPrice:
                minPrice = x

            potentialProfit = x - minPrice
            if potentialProfit > maxProfyt:
                maxProfyt = potentialProfit
        return maxProfyt