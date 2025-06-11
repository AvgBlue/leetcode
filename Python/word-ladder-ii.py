from typing import Dict, List
from collections import defaultdict


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        if endWord not in wordList:
            return []

        result: List[List[str]] = []
        parent_dict: Dict[str, List[str]] = defaultdict(list)

        def add_result(word: str):
            nonlocal beginWord, result, parent_dict, endWord
            new_list: List[str] = [endWord]
            while word != beginWord:
                new_list.append(word)
                word = parent_dict[word]
            new_list.append(beginWord)
            new_list.reverse()
            result.append(new_list)

        pattern_dict: Dict[str, List[str]] = defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                pattern_dict[pattern].append(word)

        visited = set([beginWord])
        queue: List[str] = [beginWord]

        while queue and not result:
            next_queue: List[str] = []
            for word in queue:
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1 :]
                    for neighbor in pattern_dict[pattern]:
                        if neighbor == endWord:
                            add_result(word)
                            continue
                        if neighbor not in visited:
                            visited.add(neighbor)
                            parent_dict[neighbor].append(word)
                            next_queue.append(neighbor)
            queue = next_queue

        return result


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    sol2 = Solution()
    print("All Shortest Ladders:", sol2.findLadders(beginWord, endWord, wordList))
