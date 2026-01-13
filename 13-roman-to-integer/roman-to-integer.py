class Solution:
    def romanToInt(self, s: str) -> int:
        Numerals = {
            "I": 1,
            "V":5,
            "X":10,
            "L":50,
            "C": 100,
            "D":500,
            "M":1000
        }


        total = 0

        for i in range(len(s)):
            if s[i] in Numerals:
                if i + 1 < len(s) and Numerals[s[i]] < Numerals[s[i + 1]]:
                    total -= Numerals[s[i]]
                else:
                    total += Numerals[s[i]]
        return(total)



        