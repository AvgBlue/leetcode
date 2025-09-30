from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        i = 0
        len_strs = len(strs)
        lens_strs = [len(s) for s in strs]

        def equal_at_i(i: int) -> bool:
            if lens_strs[0] <= i:
                return False
            strs0_at_i = strs[0][i]
            for j in range(1, len_strs):
                if i >= lens_strs[j] or strs[j][i] != strs0_at_i:
                    return False
            return True

        while equal_at_i(i):
            i += 1
        return strs[0][:i]


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs))
