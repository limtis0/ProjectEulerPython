from tools.compete import Compete
from tools.fibstream import FibStream


"""https://projecteuler.net/problem=25"""


class Solution:
    @staticmethod
    def solution():
        fibs = FibStream.fib_stream()
        ind, num = 1, next(fibs)
        while len(str(num)) != 1000:
            num = next(fibs)
            ind += 1
        return ind


if __name__ == '__main__':
    Compete.estimate_method(Solution.solution, repeat=10)
    print(f"\nAnswer: {Solution.solution()}")
