class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = {}

        for num in nums:
            num_dict[num] = True

        longest_seq_c_max = 0

        for num in list(num_dict.keys()):
            seq_c = 0
            while num_dict.get(num, False):
                del num_dict[num]
                num += 1
                seq_c += 1
            
            if longest_seq_c_max < seq_c:
                longest_seq_c_max = seq_c

        return longest_seq_c_max
