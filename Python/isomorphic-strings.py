class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping: dict[str, str] = {}
        seen = set()
        for c1, c2 in zip(s, t):
            if c1 not in mapping:
                if c2 in seen:
                    return False
                mapping[c1] = c2
                seen.add(c2)
            elif c1 in mapping and mapping[c1] != c2:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isIsomorphic("egg", "add"))
    print(solution.isIsomorphic("foo", "bar"))
    print(solution.isIsomorphic("paper", "title"))
    print(solution.isIsomorphic("badc", "baba"))
