from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        return 0 <= int(s) <= 255 and (s == "0" or not s.startswith("0"))

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []

        result: List[str] = []

        for i in range(1, 4):
            s1: str = s[:i]
            if not self.isValid(s1):
                continue
            s2: str = s[i:]
            for i2 in range(1, 4):
                s3: str = s2[:i2]
                if not self.isValid(s3):
                    continue
                s4: str = s2[i2:]
                for i3 in range(1, 4):
                    s5: str = s4[:i3]
                    s6: str = s4[i3:]
                    if not (self.isValid(s5) and self.isValid(s6)):
                        continue
                    result.append(f"{s1}.{s3}.{s5}.{s6}")

        return result


if __name__ == "__main__":
    solution = Solution()
    test_input = "25525511135"
    print(solution.restoreIpAddresses(test_input))
