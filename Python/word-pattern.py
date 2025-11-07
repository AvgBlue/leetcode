class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping_p_to_s: dict[str, str] = {}
        mapping_s_to_p: dict[str, str] = {}
        s_words = s.split()
        if len(s_words)!= len(pattern):
            return False
        for c, word in zip(pattern, s_words):
            if (
                mapping_p_to_s.get(c, word) != word
                or mapping_s_to_p.get(word, c) != c
            ):
                return False
            mapping_p_to_s[c] = word
            mapping_s_to_p[word] = c
        return True


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    print(solution.wordPattern("abba", "dog cat cat dog"))  # True
    print(solution.wordPattern("abba", "dog cat cat fish"))  # False
    print(solution.wordPattern("aaaa", "dog cat cat dog"))  # False
    print(solution.wordPattern("abba", "dog dog dog dog"))  # False
