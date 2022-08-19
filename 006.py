from tools.compete import Compete


""" https://projecteuler.net/problem=6 """


class Solution:
    @staticmethod
    def straight_oneliner():
        return sum(range(1, 101))**2 - sum([i**2 for i in range(1, 101)])

    @staticmethod
    def math_oneliner():
        # (1 + 2 + ... + n)^2 == n^2 * (n+1)^2 * 1/4
        # (1^2 + 2^2 + ... + n^2) == n * (n+1) * (2n+1) * 1/6
        return int((100**2 * (100+1)**2 * (1/4)) - (100 * (100+1) * (100*2+1) * (1/6)))


if __name__ == "__main__":
    Compete.compare_methods(Solution)
    print(f"Answer: {Solution.math_oneliner()}")