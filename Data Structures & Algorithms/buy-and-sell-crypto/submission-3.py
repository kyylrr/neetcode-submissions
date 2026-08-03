class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right = 1
        left = 0
        besSum =0
        while right < len(prices):
            
            if prices[left] < prices[right]:
                besSum = max(besSum, (prices[right]-prices[left]))
            else  :
                left = right
            right+=1
        return besSum
            
            