class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10

        # Count how many times each digit occurs
        for d in digits:
            freq[d] += 1

        ans = 0

        # Choose the last digit (must be even)
        for last in [0, 2, 4, 6, 8]:
            if freq[last] == 0:
                continue

            freq[last] -= 1

            # Choose the first digit (cannot be 0)
            for first in range(1, 10):
                if freq[first] == 0:
                    continue

                freq[first] -= 1

                # Choose the middle digit
                for middle in range(10):
                    if freq[middle] > 0:
                        ans += 1

                freq[first] += 1

            freq[last] += 1

        return ans