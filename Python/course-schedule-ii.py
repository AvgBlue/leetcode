from collections import defaultdict
from typing import Dict, List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        tree: Dict[int, List[int]] = defaultdict(list)
        for courses, need_to_take_courses in prerequisites:
            tree[need_to_take_courses].append(courses)
        result = []
        visited = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited

        def dfs(node):
            if visited[node] == 1:
                return False  # cycle detected
            if visited[node] == 2:
                return True
            visited[node] = 1
            for neighbor in tree[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2
            result.append(node)
            return True

        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []
        result.reverse()

        return result


if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    sol = Solution()
    order = sol.findOrder(numCourses, prerequisites)
    print("Order to take courses:", order)
