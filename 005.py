from tools.compete import Compete
from tools.primestream import PrimeStream


""" https://projecteuler.net/problem=5 """


class Solution:
    @staticmethod
    def bruteforce():
        n = 20
        while True:
            if all(n % i == 0 for i in range(2, 21)):
                return n
            n += 20

    @staticmethod
    def primes():
        stream = PrimeStream.prime_stream(100)
        num = 1
        while True:  # While i < 20
            prime = next(stream)
            if prime > 20:
                break
            j = 1
            while prime**j < 20:
                j += 1
            num *= prime**(j-1)
        return num


if __name__ == "__main__":
    Compete.compare_methods(Solution, repeat=2)
    print(f"\nAnswer: {Solution.primes()}")
