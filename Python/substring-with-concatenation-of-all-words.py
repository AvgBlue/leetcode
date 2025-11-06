from collections import defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_s = len(s)
        len_words = len(words)
        len_word = len(words[0])
        result: List[int] = []

        words_dict: dict[str, int] = defaultdict(int)
        for w in words:
            words_dict[w] += 1

        def window_start_at_i(i):
            words_dict_copy = dict(words_dict)

            def contain_all():
                for key in words_dict_copy:
                    if words_dict_copy[key] != 0:
                        return False
                return True

            # fist window
            for j in range(i, i + len_words * len_word, len_word):
                if s[j : j + len_word] in words_dict_copy:
                    words_dict_copy[s[j : j + len_word]] -= 1
            if contain_all():
                result.append(i)
            start = i
            end = i + len_words * len_word
            # second window on word
            while end < len_s:
                if s[start : start + len_word] in words_dict_copy:
                    words_dict_copy[s[start : start + len_word]] += 1
                start += len_word
                if s[end : end + len_word] in words_dict_copy:
                    words_dict_copy[s[end : end + len_word]] -= 1
                end += len_word
                if contain_all():
                    result.append(start)

        for i in range(len_word):
            window_start_at_i(i)
        return result


if __name__ == "__main__":
    solution = Solution()
    # Test case 1
    s1 = "barfoothefoobarman"
    words1 = ["foo", "bar"]
    print(f'Input: s = "{s1}", words = {words1}')
    print(f"Output: {solution.findSubstring(s1, words1)}")
    print()

    # Test case 2
    s2 = "wordgoodgoodgoodbestword"
    words2 = ["word", "good", "best", "word"]
    print(f'Input: s = "{s2}", words = {words2}')
    print(f"Output: {solution.findSubstring(s2, words2)}")
    print()

    # Test case 3
    s3 = "barfoofoobarthefoobarman"
    words3 = ["bar", "foo", "the"]
    print(f'Input: s = "{s3}", words = {words3}')
    print(f"Output: {solution.findSubstring(s3, words3)}")
