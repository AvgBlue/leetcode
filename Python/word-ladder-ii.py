from ast import Dict
from collections import defaultdict
from typing import List


class Solution:
        self_neighbors_dict: Dict[str, List[str]] = defaultdict(list)

        def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
            if endWord not in wordList:
                return 0

            neighbors_dict: Dict[str, List[str]] = defaultdict(list)
            self.self_neighbors_dict=neighbors_dict
            for word in wordList + [beginWord]:
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    neighbors_dict[pattern].append(word)

            visited = {beginWord}
            curr_level = [beginWord]

            steps = 1

            while curr_level:
                next_level = []

                for word1 in curr_level:
                    for i in range(len(word1)):
                        pattern = word1[:i] + "*" + word1[i + 1:]

                        for word2 in neighbors_dict[pattern]:
                            if word2 == endWord:
                                return steps + 1

                            if word2 not in visited:
                                visited.add(word2)
                                next_level.append(word2)

                curr_level = next_level
                steps += 1

            return 0

        def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
            length=self.ladderLength(beginWord,endWord,wordList)
            
            neighbors_dict=self.self_neighbors_dict
            paths_from_beginWord=[[beginWord]]
            paths_from_endWord=[[endWord]]

            edges = length - 1
            
            begin_depth = edges // 2
            end_depth = edges - begin_depth
            for _ in range(begin_depth):
                next_path_list=[]
                for path in paths_from_beginWord:
                    last_word=path[-1]
                    for i in range(len(last_word)):
                        pattern = last_word[:i] + "*" + last_word[i + 1:]
                        for next_word in neighbors_dict[pattern]:

                            if next_word not in path:
                                next_path_list.append(path+[next_word])
                paths_from_beginWord=next_path_list

            for _ in range(end_depth):
                next_path_list=[]
                for path in paths_from_endWord:
                    last_word=path[-1]
                    for i in range(len(last_word)):
                        pattern = last_word[:i] + "*" + last_word[i + 1:]
                        for next_word in neighbors_dict[pattern]:

                            if next_word not in path:
                                next_path_list.append(path+[next_word])
                paths_from_endWord=next_path_list


            paths_from_beginWord_end_dict = defaultdict(list)

            for path in paths_from_beginWord:
                paths_from_beginWord_end_dict[path[-1]].append(path)

            result = set()

            for end_path in paths_from_endWord:
                middle = end_path[-1]

                for begin_path in paths_from_beginWord_end_dict[middle]:
                    result.add(tuple(begin_path + list(reversed(end_path[:-1]))))

            
            return [list(path) for path in result]


def run_tests():
    sol = Solution()

    tests = [
        (
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log", "cog"],
            [
                ["hit", "hot", "dot", "dog", "cog"],
                ["hit", "hot", "lot", "log", "cog"],
            ],
        ),
        (
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log"],
            [],
        ),
        (
            "a",
            "c",
            ["a", "b", "c"],
            [
                ["a", "c"],
            ],
        ),
        (
            "red",
            "tax",
            ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"],
            [
                ["red", "ted", "tad", "tax"],
                ["red", "ted", "tex", "tax"],
                ["red", "rex", "tex", "tax"],
            ],
        ),
    ]

    failed = 0

    for i, (beginWord, endWord, wordList, expected) in enumerate(tests, start=1):
        result = sol.findLadders(beginWord, endWord, wordList)

        # Order of paths does not matter
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)

        print(f"Test {i}")
        print(f"begin:    {beginWord}")
        print(f"end:      {endWord}")
        print(f"result:   {result}")
        print(f"expected: {expected}")

        if result_sorted == expected_sorted:
            print("Passed\n")
        else:
            print("FAILED")

            result_set = {tuple(path) for path in result}
            expected_set = {tuple(path) for path in expected}

            print(f"missing: {expected_set - result_set}")
            print(f"extra:   {result_set - expected_set}\n")

            failed += 1

    print(f"{len(tests) - failed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()