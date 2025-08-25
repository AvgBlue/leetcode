class Solution:
    units = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
    }
    tens = {
        1: "X",
        2: "XX",
        3: "XXX",
        4: "XL",
        5: "L",
        6: "LX",
        7: "LXX",
        8: "LXXX",
        9: "XC",
    }
    hundreds = {
        1: "C",
        2: "CC",
        3: "CCC",
        4: "CD",
        5: "D",
        6: "DC",
        7: "DCC",
        8: "DCCC",
        9: "CM",
    }
    thousands = {1: "M", 2: "MM", 3: "MMM"}

    def intToRoman(self, num: int) -> str:
        result = ""
        if num >= 1000:
            result += self.thousands.get(num // 1000, "")
        if num >= 100:
            result += self.hundreds.get((num % 1000) // 100, "")
        if num >= 10:
            result += self.tens.get((num % 100) // 10, "")
        result += self.units.get(num % 10, "")
        return result
