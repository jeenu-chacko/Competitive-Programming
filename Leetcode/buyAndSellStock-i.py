class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum,maximumProfit= float('inf'),0
        for price in prices:
            minimum=min(price,minimum)
            maximumProfit=max(maximumProfit,price-minimum)
        return maximumProfit
            
