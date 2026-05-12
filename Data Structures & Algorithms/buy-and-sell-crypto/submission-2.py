class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentprof = 0
        maxprof = 0

        left = 0
        right = 1

        while(right < len(prices)):
            if(prices[left] < prices[right]):
                currentprof = prices[right] - prices[left]
                maxprof = max(maxprof, currentprof)
            else:
                left = right
            right += 1

        return maxprof