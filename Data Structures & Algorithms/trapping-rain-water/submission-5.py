class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1

        while l < r and height[l] <= height[l + 1]:
            l += 1

        while r > l and height[r] <= height[r - 1]:
            r -= 1

        result = 0

        while l < r:
            tmp_l = l
            while tmp_l < r and height[tmp_l + 1] < height[l]:
                tmp_l += 1

            last_reached = tmp_l == r

            if last_reached:
                min_pole = height[tmp_l]
                for i in range(l + 1, r):
                    if min_pole - height[i] > 0:
                        result += min_pole - height[i]

                l = tmp_l
            else:
                for i in range(l + 1, tmp_l + 1):
                    result += height[l] - height[i]
                l = tmp_l + 1

            tmp_r = r
            while tmp_r > l and height[tmp_r - 1] < height[r]:
                tmp_r -= 1
            
            for i in range(r - 1, tmp_r - 1, -1):
                result += height[r] - height[i]

            r = tmp_r - 1

        return result