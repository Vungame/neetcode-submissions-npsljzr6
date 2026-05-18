class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentProf = 0
        maxProf = 0
        left = 0
        right = 1

        while (right < len(prices)):
            if(prices[left] < prices[right]):
                currentProf = prices[right] - prices[left]
                maxProf = max(maxProf, currentProf)
            else:
                left = right
            right += 1
        return maxProf