from ast import Dict, List
from typing import Optional
from collections import defaultdict


from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neighbors_dict: Dict[str, List[str]] = defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                neighbors_dict[pattern].append(word)

        visited1 = set([beginWord])
        visited2 = set([endWord])
        curr_level1: List[str] = [beginWord]
        curr_level2: List[str] = [endWord]

        steps = 1

        while curr_level1 and curr_level2:
            if len(curr_level1) > len(curr_level2):
                curr_level1, curr_level2 = curr_level2, curr_level1
                visited1, visited2 = visited2, visited1
            next_level: List[str] = []

            for word1 in curr_level1:
                for i in range(len(word1)):
                    pattern = word1[:i] + "*" + word1[i + 1 :]
                    for word2 in neighbors_dict[pattern]:
                        if word2 not in visited1:
                            if word2 in visited2:
                                return steps + 1
                            next_level.append(word2)
                            visited1.add(word2)
            curr_level1 = next_level
            steps += 1

        return 0


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    sol = Solution()
    result = sol.ladderLength(beginWord, endWord, wordList)
    print("Ladder Length:", result)
