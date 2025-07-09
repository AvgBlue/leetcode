from typing import Deque, Dict
from collections import deque, Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        freq_dict_target: Dict[str, int] = Counter(t)
        target = len(freq_dict_target)
        freq_dict: Dict[str, int] = {c: 0 for c in t}

        # step 1 build first window
        start: int = 0
        end: int = 0
        for c in s:
            if c in freq_dict:
                freq_dict[c] += 1
                if freq_dict[c] == freq_dict_target[c]:
                    target -= 1
            end += 1
            if target == 0:
                break

        if target != 0:
            return ""
        min_window_len = end - start
        min_start: int = start
        min_end: int = end

        # step 2 running on the window
        for c in s[end:]:
            while target == 0:
                if end - start < min_window_len:
                    min_window_len = end - start
                    min_start, min_end = start, end
                if s[start] in freq_dict:
                    if freq_dict[s[start]] == freq_dict_target[s[start]]:
                        target += 1
                    freq_dict[s[start]] -= 1
                start += 1
            end += 1
            if c in freq_dict:
                freq_dict[c] += 1
                if freq_dict[c] == freq_dict_target[c]:
                    target -= 1
            if target == 0 and end - start < min_window_len:
                min_window_len = end - start
                min_start, min_end = start, end

        while target == 0:
            if end - start < min_window_len:
                min_window_len = end - start
                min_start, min_end = start, end
            if s[start] in freq_dict:
                if freq_dict[s[start]] == freq_dict_target[s[start]]:
                    target += 1
                freq_dict[s[start]] -= 1
            start += 1
        return s[min_start:min_end]


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    target = Counter("aaaaaaa")
    required = len(target)
    print(required)
    result = Solution().minWindow(s, t)
    print(result)
