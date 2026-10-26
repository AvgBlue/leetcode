from collections import deque
import re


class Solution:


    def decodeString(self, s: str) -> str:
        result=""
        stack=deque()
        len_s=len(s)

        def get_inner(start:int)->str:
                result=""
                count=0
                is_do=True
                i=start
                while is_do or count>0:
                    is_do=False
                    c=s[i]
                    result+=c
                    if '['==c:
                        count+=1
                    elif ']'==c:
                        count-=1
                    i+=1
                return result

        i=0
        
        while i<len_s:
            c=s[i]
            if c.isdigit():
                match=re.search(r"\d+",s[i:])
                stack.append(match.group())
            elif c.isalpha():
                match=re.search(r"[a-z]+",s[i:])
                stack.append(match.group())
            elif c=='[':
                stack.append(get_inner(i))
            i+=len(stack[-1])

        while stack:
            head:str=stack.popleft()
            if head.isdigit():
                number=int(head)
                inner=stack.popleft()
                inner_decoded=self.decodeString(inner[1:-1])
                result+=number*inner_decoded
            if head.isalpha():
                result+=head
        return result




def run_tests():
    sol = Solution()

    tests = [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("abc3[cd]xyz", "abccdcdcdxyz"),
        ("10[a]", "aaaaaaaaaa"),
        ("2[a2[b]c]", "abbcabbc"),
        ("a", "a"),
    ]

    failed = 0

    for i, (s, expected) in enumerate(tests, start=1):
        result = sol.decodeString(s)

        print(f"Test {i}: {s!r}")
        print(f"result:   {result!r}")
        print(f"expected: {expected!r}")

        if result == expected:
            print("Passed\n")
        else:
            print("FAILED\n")
            failed += 1

    print(f"{len(tests) - failed}/{len(tests)} tests passed")

    if failed:
        print(f"{failed} tests failed")
    else:
        print("All tests passed!")


if __name__ == "__main__":
    run_tests()


