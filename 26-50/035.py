from collections import deque
from tools.compete import Compete
from tools.primestream import PrimeStream


''' https://projecteuler.net/problem=35 '''


class Solution:
    @staticmethod
    def _fully_odd(num: int):
        if num == 2:
            return True
        for dig in str(num):
            if dig in ('0', '2', '4', '8'):
                return False
        return True

    @staticmethod
    def _rotations(num: int):
        digits = deque([int(i) for i in str(num)])
        for i in range(len(digits)):
            yield int(''.join(map(str, digits)))
            digits.rotate()

    @staticmethod
    def solution():
        primes = {i for i in PrimeStream(1_000_000) if Solution._fully_odd(i)}
        count = 0
        while primes:
            circular = True
            prime = primes.pop()
            rotations = set(i for i in Solution._rotations(prime))
            for rot in rotations:
                if rot != prime and rot not in primes:
                    circular = False
                    break
            if circular:
                count += len(rotations)
            primes = primes.difference(rotations)
        return count


if __name__ == '__main__':
    Compete.estimate_method(Solution.solution, repeat=3)
    print(f'\nAnswer: {Solution.solution()}')
