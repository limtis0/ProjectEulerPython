from tools.compete import Compete
from tools.primestream import PrimeStream


''' https://projecteuler.net/problem=26 '''


class Solution:
    @staticmethod
    def _get_cycle_size(div, num=1):
        d = {}
        ind = 0
        while num != 0:
            num = num * 10 % div
            if num in d:
                return ind - d[num]
            d[num] = ind
            ind += 1
        return 0

    @staticmethod
    def solution():
        cycles = [(Solution._get_cycle_size(i), i) for i in range(2, 1000)]
        return max(cycles, key=lambda item: item[0])[1]

    @staticmethod
    def solution_primes():
        stream = PrimeStream(1000)
        cycles = []
        while (i := next(stream, None)) is not None:
            cycles.append((Solution._get_cycle_size(i), i))
        return max(cycles, key=lambda item: item[0])[1]


if __name__ == '__main__':
    Compete.compare_methods(Solution, repeat=50)
    print(f'\nAnswer: {Solution.solution_primes()}')
