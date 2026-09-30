class Solution:
    def is_sorted(self, word_a, word_b, char_dict):
        len_a, len_b = len(word_a), len(word_b)

        for i in range(min(len_a, len_b)):
            if char_dict[word_a[i]] > char_dict[word_b[i]]:
                return False
            elif char_dict[word_a[i]] < char_dict[word_b[i]]:
                return True
            
            if char_dict[word_a[i]] != char_dict[word_b[i]]:
                all_equal = False

        if len_a > len_b:
            return False

        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_index = dict()

        for idx, ch in enumerate(order):
            char_index[ch] = idx

        words_len = len(words)

        for i in range(words_len - 1):
            if not self.is_sorted(words[i], words[i+1], char_index):
                return False

        return True