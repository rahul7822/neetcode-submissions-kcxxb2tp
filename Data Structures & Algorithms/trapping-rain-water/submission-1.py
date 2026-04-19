class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1

        while l < r and height[l] < height[l + 1]:
            l += 1

        while r > l and height[r] < height[r - 1]:
            r -= 1

        result = 0

        while l < r:
            tmp_l = l
            while tmp_l < r and height[tmp_l + 1] < height[l]:
                tmp_l += 1

            for i in range(l + 1, tmp_l + 1):
                result += height[l] - height[i]
            
            l = tmp_l + 1

        return result

        

        