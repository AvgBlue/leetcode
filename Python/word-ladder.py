from ast import Dict, List
from typing import Optional
from collections import defaultdict


from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def hamming_distance(word1: str, word2: str) -> int:
            return sum(c1 != c2 for c1, c2 in zip(word1, word2))

        def in_matrix(word1: str, word2: str) -> bool:
            return word1 != word2 and hamming_distance(word1, word2) == 1

        neighbors_dict: Dict[str, List[str]] = defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                neighbors_dict[pattern].append(word)

        visited = set()
        curr_level: List[str] = [beginWord]
        steps = 1

        while curr_level:
            next_level: List[str] = []
            for word1 in curr_level:
                for i in range(len(word1)):
                    pattern = word1[:i] + "*" + word1[i + 1 :]
                    for word2 in neighbors_dict[pattern]:
                        if word2 not in visited:
                            if word2 == endWord:
                                return steps + 1
                            next_level.append(word2)
                            visited.add(word2)
            curr_level = next_level
            steps += 1

        return 0


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    sol = Solution()
    result = sol.ladderLength(beginWord, endWord, wordList)
    print("Ladder Length:", result)
