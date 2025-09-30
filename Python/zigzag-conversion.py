from pyparsing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s_len = len(s)
        lines: List[str] = [""] * numRows
        index: int = 0
        direction: int = 1  # 1 forword -1 backward
        line_index = 0
        while index < s_len:
            lines[line_index] += s[index]
            line_index += direction
            if line_index < 0 or line_index >= numRows:
                direction *= -1
                line_index += 2*direction
            index += 1
        return "".join(lines)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    solution = Solution()
    result = solution.convert(s, numRows)
    print(result)
