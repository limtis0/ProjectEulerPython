from tools.compete import Compete
from tools.primestream import PrimeStream


''' https://projecteuler.net/problem=7 '''


class Solution:
    @staticmethod
    def sieve():
        stream = PrimeStream(1000000)
        for _ in range(10_000):
            next(stream)
        return next(stream)


if __name__ == '__main__':
    Compete.estimate_method(Solution.sieve)
    print(f'\nAnswer: {Solution.sieve()}')
