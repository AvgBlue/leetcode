from typing import Dict, List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return self.boyer_moore_search(haystack, needle, find_all=False)

    def boyer_moore_search(
        self, text: str, pattern: str, *, find_all: bool = False
    ) -> int | List[int]:
        """
        Boyer–Moore substring search.
        Returns the first match index by default, or a list of all match indices if find_all=True.
        Raises ValueError on empty pattern.

        >>> boyer_moore_search("abracadabra", "abra")
        0
        >>> boyer_moore_search("abracadabra", "abra", find_all=True)
        [0, 7]
        >>> boyer_moore_search("aaaaa", "aa", find_all=True)
        [0, 1, 2, 3]
        >>> boyer_moore_search("hello", "world")
        -1
        """
        if pattern == "":
            raise ValueError("pattern must be non-empty")

        n, m = len(text), len(pattern)
        if m > n:
            return [] if find_all else -1

        last: Dict[str, int] = self._build_bad_char_table(pattern)
        suffix, prefix = self._build_good_suffix_tables(pattern)

        results: List[int] = []
        i = 0
        while i <= n - m:
            j = m - 1
            # scan from right to left
            while j >= 0 and text[i + j] == pattern[j]:
                j -= 1

            if j < 0:
                # match found
                if find_all:
                    results.append(i)
                    # shift to look for next (allow overlaps)
                    i += m if m == 1 else self._next_shift_after_match(m, prefix)
                    continue
                return i

            # mismatch at pattern[j] vs text[i+j]
            bad_char_shift = j - last.get(text[i + j], -1)

            good_suffix_shift = 0
            k = m - 1 - j  # length of the matched suffix at the right
            if k > 0:
                if suffix[k] != -1:  # a substring occurs elsewhere
                    good_suffix_shift = j - suffix[k] + 1
                else:
                    # move pattern so that a prefix of pattern matches the good suffix
                    for r in range(j + 2, m):
                        if prefix[m - r]:
                            good_suffix_shift = r
                            break
                    if good_suffix_shift == 0:
                        good_suffix_shift = m
            else:
                # when mismatch is at the last char, good-suffix gives no info
                good_suffix_shift = 1

            i += max(bad_char_shift, good_suffix_shift)

        return results if find_all else -1

    def _build_bad_char_table(self, p: str) -> Dict[str, int]:
        """Last occurrence of each char in pattern."""
        last: Dict[str, int] = {}
        for i, ch in enumerate(p):
            last[ch] = i
        return last

    def _build_good_suffix_tables(self, p: str) -> tuple[list[int], list[bool]]:
        """
        Build the 'suffix' and 'prefix' tables used for the good-suffix rule.
        suffix[k] = start index in p of a substring that matches the last k chars of p; -1 if none.
        prefix[k] = True if a prefix of p matches the last k chars of p.
        """
        m = len(p)
        suffix = [-1] * m
        prefix = [False] * m
        for i in range(m - 1):  # end at m-2
            j = i
            k = 0
            while j >= 0 and p[j] == p[m - 1 - k]:
                j -= 1
                k += 1
                suffix[k] = j + 1  # record the start index
            if j == -1:
                prefix[k] = True
        return suffix, prefix

    def _next_shift_after_match(self, m: int, prefix: List[bool]) -> int:
        """
        When a full match is found, decide how far to shift to search for another match
        (this enables finding overlapping matches).
        """
        # Find the longest prefix that is also a suffix to allow overlap
        for k in range(m - 1, 0, -1):
            if prefix[k]:
                return m - k
        return m


if __name__ == "__main__":
    haystack = "abracadabra"
    needle = "abra"
    sol = Solution()
    print(
        f"First occurrence of '{needle}' in '{haystack}': {sol.strStr(haystack, needle)}"
    )
    print(
        f"All occurrences of '{needle}' in '{haystack}': {sol.boyer_moore_search(haystack, needle, find_all=True)}"
    )
