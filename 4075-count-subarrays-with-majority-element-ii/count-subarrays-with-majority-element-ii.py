from typing import List

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, idx, delta):
        while idx < len(self.bit):
            self.bit[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & -idx
        return res


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        prefix = 0
        prefixes = [0]

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1
            prefixes.append(prefix)

        vals = sorted(set(prefixes))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        bit = Fenwick(len(vals))
        ans = 0

        for p in prefixes:
            idx = rank[p]
            ans += bit.query(idx - 1)  
            bit.update(idx, 1)

        return ans