class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(index, cur_sum, subset):
            if cur_sum == target:
                result.append(subset.copy())

            if cur_sum > target:
                return

            for i in range(index, len(nums)):
                if cur_sum + nums[i] <= target:
                    subset.append(nums[i])
                    backtrack(i, cur_sum + nums[i], subset)
                    subset.pop()

        backtrack(0, 0, [])
        return result