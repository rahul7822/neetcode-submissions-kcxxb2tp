class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        index_dict = {}

        for i in range(len_nums):
            num = nums[i]
            if i == 0:
                index_dict[num] = i

            rem = target - nums[i]
            rem_index = index_dict.get(rem, -1)

            if rem_index != -1 and rem_index != i:
                return [rem_index, i]
            else:
                index_dict[num] = i