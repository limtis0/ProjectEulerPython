from tools.compete import Compete
from functools import lru_cache
from sys import setrecursionlimit


""" https://projecteuler.net/problem=14 """


class Solution:
    @staticmethod
    @lru_cache(maxsize=None)
    def _memo_ez(n, count=1):
        if n == 1:
            return count
        return Solution._memo_ez(3*n+1, count+1) if n % 2 else Solution._memo_ez(n//2, count+1)

    @staticmethod
    def memo_ez():
        m = ans = 1
        for i in range(1, 1_000_001):
            chain_size = Solution._memo_ez(i)
            if m < chain_size:
                m = chain_size
                ans = i
        return ans

    @staticmethod
    def memo_no_rec():
        memo = {}
        for i in range(1, 1_000_001):
            chain = 1
            cur_num = i
            while cur_num != 1:
                if cur_num in memo:
                    chain += memo[cur_num]
                    break
                cur_num = 3 * cur_num + 1 if cur_num % 2 else cur_num // 2
                chain += 1
            memo[i] = chain
        return max(memo, key=memo.get)


if __name__ == "__main__":
    setrecursionlimit(2000)

    Compete.compare_methods(Solution, repeat=2)
    print(f"\nAnswer: {Solution.memo_no_rec()}")
