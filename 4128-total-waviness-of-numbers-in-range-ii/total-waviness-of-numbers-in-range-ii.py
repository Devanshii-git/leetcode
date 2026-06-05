from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n: int) -> int:
            if n < 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dfs(pos, tight, started, length_state, last2, last1):
                """
                Returns:
                    (count_numbers, total_waviness_sum)
                length_state:
                    0 -> no digit chosen yet
                    1 -> exactly one actual digit seen
                    2 -> at least two actual digits seen
                """

                if pos == m:
                    return (1, 0)

                limit = digits[pos] if tight else 9

                total_cnt = 0
                total_wavy = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    # Still skipping leading zeros
                    if not started and d == 0:
                        cnt, wav = dfs(
                            pos + 1,
                            ntight,
                            False,
                            0,
                            10,
                            10
                        )
                        total_cnt += cnt
                        total_wavy += wav
                        continue

                    # Starting the number
                    if not started:
                        cnt, wav = dfs(
                            pos + 1,
                            ntight,
                            True,
                            1,
                            10,
                            d
                        )
                        total_cnt += cnt
                        total_wavy += wav
                        continue

                    # Already started
                    if length_state == 1:
                        cnt, wav = dfs(
                            pos + 1,
                            ntight,
                            True,
                            2,
                            last1,
                            d
                        )
                        total_cnt += cnt
                        total_wavy += wav

                    else:  # length_state == 2
                        a, b = last2, last1

                        add = 1 if ((b > a and b > d) or
                                    (b < a and b < d)) else 0

                        cnt, wav = dfs(
                            pos + 1,
                            ntight,
                            True,
                            2,
                            b,
                            d
                        )

                        total_cnt += cnt
                        total_wavy += wav + add * cnt

                return (total_cnt, total_wavy)

            return dfs(0, True, False, 0, 10, 10)[1]

        return solve(num2) - solve(num1 - 1)