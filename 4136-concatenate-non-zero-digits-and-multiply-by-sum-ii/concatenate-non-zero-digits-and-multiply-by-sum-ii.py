from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        # Store only non-zero digits and their positions
        pos = []
        digits = []
        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        n = len(digits)

        # powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # Prefix value of non-zero digit sequence
        prefVal = [0] * (n + 1)
        # Prefix digit sum
        prefSum = [0] * (n + 1)

        for i in range(n):
            prefVal[i + 1] = (prefVal[i] * 10 + digits[i]) % MOD
            prefSum[i + 1] = prefSum[i] + digits[i]

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r)

            if left == right:
                ans.append(0)
                continue

            length = right - left

            # Value of concatenated non-zero digits in the range
            x = (prefVal[right] - prefVal[left] * pow10[length]) % MOD

            # Sum of digits
            digit_sum = prefSum[right] - prefSum[left]

            ans.append((x * digit_sum) % MOD)

        return ans