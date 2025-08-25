from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        len_ratings: int = len(ratings)
        candies = [1] * len_ratings
        for j in range(1, len_ratings):
            if ratings[j - 1] < ratings[j]:
                candies[j] = max(candies[j - 1] + 1, candies[j])
            i = len_ratings - 1 - j
            if ratings[i + 1] < ratings[i]:
                candies[i] = max(candies[i + 1] + 1, candies[i])
        return sum(candies)


if __name__ == "__main__":
    ratings = [1, 0, 2]
    solution = Solution()
    result = solution.candy(ratings)
    print(result)
