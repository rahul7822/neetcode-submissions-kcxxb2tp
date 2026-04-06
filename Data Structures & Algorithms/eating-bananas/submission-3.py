class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = r

        while l <= r:
            m = (l + r) // 2
            hours_taken = self.hoursTakenToEat(m, piles)

            if hours_taken <= h:
                min_k = min(min_k, m)
                r = m - 1
            else:
                l = m + 1
                
        
        return min_k


    def hoursTakenToEat(self, rate, piles):
        result = sum(map(lambda x : math.ceil(x / rate), piles))
        return result
        