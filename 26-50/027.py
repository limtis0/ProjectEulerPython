from tools.compete import Compete
from tools.primestream import PrimeStream


''' https://projecteuler.net/problem=27 '''


class Solution:
    primes = set(PrimeStream(1_000_000))

    @staticmethod
    def _check_primes(a, b):
        count = 0
        while count*count + a*count + b in Solution.primes:
            count += 1
        return count

    @staticmethod
    def bruteforce():
        max_primes = 0
        prod = 0
        for a in range(-999, 1000):
            for b in range(-1000, 1001):
                count_primes = Solution._check_primes(a, b)
                if max_primes < count_primes:
                    max_primes = count_primes
                    prod = a * b
        return prod

    primes_b = list(PrimeStream(1000))

    @staticmethod
    def bruteforce_short():  # You can notice that b number must be prime (otherwise it won't work with x=0)
        max_primes = 0
        prod = 0
        for a in range(-999, 1000):
            for b in Solution.primes_b:
                count_primes = Solution._check_primes(a, b)
                if max_primes < count_primes:
                    max_primes = count_primes
                    prod = a * b
        return prod


if __name__ == '__main__':
    Compete.compare_methods(Solution, repeat=3)
    print(f'\nAnswer: {Solution.bruteforce_short()}')
