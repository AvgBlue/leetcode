class Solution:
    def reverseWords(self, s: str) -> str:
        len_s = len(s)
        index = 0
        words = []
        word = ""
        while index < len_s:
            if s[index] != " ":
                word += s[index]
                index += 1
            elif word == "":
                index += 1
            else:
                words.append(word)
                word = ""
        else:
            if word != "":
                words.append(word)

        words.reverse()
        return " ".join(words)


if __name__ == "__main__":
    s = "the sky is blue"
    solution = Solution()
    print(f"|{solution.reverseWords(s)}|")
