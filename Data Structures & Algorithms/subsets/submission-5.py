class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      result = []

      def backtrack(index, subset):
        if index == len(nums):
            result.append(subset.copy())
            return

        # include
        subset.append(nums[index])
        backtrack(index + 1, subset)

        # exclude
        subset.pop()
        backtrack(index + 1, subset)

      backtrack(0, [])
      return result