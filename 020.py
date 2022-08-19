from tools.compete import Compete
from math import factorial

""" https://projecteuler.net/problem=20 """


class Solution:
    @staticmethod
    def oneliner():
        return sum(int(i) for i in str(factorial(100)))

    @staticmethod
    def oneliner_map():
        return sum(map(int, str(factorial(100))))


if __name__ == "__main__":
    Compete.compare_methods(Solution)
    print(f"\nAnswer: {Solution.oneliner_map()}")
