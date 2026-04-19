class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                tmp = nums[i : j + 1]
                result.add(tuple(tmp))
        
        step = 1
        while step < len(nums):
            for i in range(len(nums)):
                for j in range(i, len(nums)):
                    tmp = nums[i : j + 1 : step]
                    result.add(tuple(tmp))
            step += 1

        result = list(map(lambda x : list(x), result))
        result.append([])
        return result