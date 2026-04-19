class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(cur, cur_index, cur_sum):
            if cur_sum > target:
                return

            if cur_sum == target:
                result.append(cur.copy())
                return

            for i in range(cur_index, len(nums)):
                cur.append(nums[i])
                backtrack(cur, i, cur_sum + nums[i])
                cur.pop()

        backtrack([], 0, 0)
        return result
