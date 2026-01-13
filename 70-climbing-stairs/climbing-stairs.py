class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        a = 1  # ways to reach step 1
        b = 2  # ways to reach step 2

        for _ in range(3, n + 1):
            c = a + b
            a = b
            b = c

        return b