from typing import List


class Solution:

    def hIndex(self, citations: List[int]) -> int:
        len_citations = len(citations)
        citations.sort()  
        for i in range(len_citations):
            if citations[i] >= len_citations - i:
                return len_citations - i
        return 0


if __name__ == "__main__":
    citations = [([3,0,6,1,5],3),([1, 3, 1],1)]
    sol = Solution()
    for x,y in citations:
        print(sol.hIndex(x) == y)
    
