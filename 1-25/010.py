from tools.compete import Compete
from tools.primestream import PrimeStream


''' https://projecteuler.net/problem=10 '''


class Solution:
    @staticmethod
    def sieve():
        stream = PrimeStream(500_000_000)
        return sum([i for i in stream])


if __name__ == '__main__':
    Compete.estimate_method(Solution.sieve, repeat=1)
    print(f'\nAnswer: {Solution.sieve()}')
