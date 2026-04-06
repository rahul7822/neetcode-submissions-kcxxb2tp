class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = {}

        for num in nums:
            num_dict[num] = True

        longest_seq_c_max = 0

        nums = num_dict.keys()
        for num in nums:
            seq_c = 0

            if num_dict.get(num - 1, False) == False:
                while num_dict.get(num, False):
                    num += 1
                    seq_c += 1
                
                if longest_seq_c_max < seq_c:
                    longest_seq_c_max = seq_c

                if len(nums) - longest_seq_c_max <= 0:
                    break

        return longest_seq_c_max
