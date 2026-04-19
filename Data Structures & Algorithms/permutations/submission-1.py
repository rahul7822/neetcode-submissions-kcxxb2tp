class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        taken = [False] * len(nums)
        def backtrack(permu):
            if len(permu) == len(nums):
                result.append(permu.copy())
                return

            for i in range(0, len(nums)):
                if not taken[i]:
                    permu.append(nums[i])
                    taken[i] = True
                    backtrack(permu)
                    permu.pop()
                    taken[i] = False

        backtrack([])
        return result