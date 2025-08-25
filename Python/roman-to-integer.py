from typing import Dict


class Solution:
    def romanToInt(self, s: str) -> int:
        len_s = len(s)
        numbers: Dict[str, int] = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        result = 0
        head: str = ""
        i = 0
        while i < len_s:
            head = s[i]
            i += 1
            if i < len_s and s[i] != head and head + s[i] in numbers:
                result += numbers[head + s[i]]
                i += 1
                continue
            result += numbers[head]
        return result


if __name__ == "__main__":
    inputs = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("MMXXIV", 2024),
        ("MMMCMXCIX", 3999),
        ("MMMDCCCLXXXVIII", 3888),
        ("MMMMCMXCIX", 4999),
        ("MMMMMM", 6000),
        ("MMMMMMMMMMCMXCIX", 10999),
    ]
    solution = Solution()
    for s in inputs:
        print(f"{s[1]}: {solution.romanToInt(s[0])}")
