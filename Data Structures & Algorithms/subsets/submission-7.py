class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index, subset):
            if index > len(nums):
                return

            result.append(subset.copy())

            for i in range(index, len(nums)):
                subset.append(nums[i]) # choose
                backtrack(i + 1, subset) # explore

                subset.pop() # undo/unchoose

        backtrack(0, [])
        return result