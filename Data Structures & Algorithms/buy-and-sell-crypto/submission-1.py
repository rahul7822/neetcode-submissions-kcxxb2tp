class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        l = len(prices)

        i, j = 0, 1
        while j < l:
            if prices[i] >= prices[j]:
                i += 1
                j += 1
            else:
                diff = prices[j] - prices[i]
                if diff > result:
                    result = diff
                j += 1


        return result

            
