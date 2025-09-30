from pyparsing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        len_words = len(words)
        list_len_words: List[int] = [len(w) for w in words]
        result: List[str] = []
        index = 0

        line_len = 0
        newLine: List[str] = []
        while index < len_words:

            # newLine is empty
            if line_len == 0:
                newLine = [words[index]]
                line_len = list_len_words[index]
            # posible to add to new line
            elif line_len + list_len_words[index] + 1 <= maxWidth:
                newLine += [" ", words[index]]
                line_len += 1 + list_len_words[index]
            # not possible
            else:
                if line_len != maxWidth:
                    # one word
                    if len(newLine) == 1:
                        newLine += [" " * (maxWidth - line_len)]
                    else:
                        while line_len < maxWidth:
                            for i in range(1, len(newLine), 2):
                                newLine[i] += " "
                                line_len += 1
                                if line_len == maxWidth:
                                    break

                result.append("".join(newLine))
                line_len = list_len_words[index]
                newLine: List[str] = [words[index]]
            index += 1
        else:
            if line_len:
                if line_len != maxWidth:
                    newLine += [" " * (maxWidth - line_len)]
                result.append("".join(newLine))

        return result


if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    sol = Solution()
    justified = sol.fullJustify(words, maxWidth)
    for line in justified:
        print(f'"{line}"')
