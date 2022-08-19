from tools.compete import Compete
from tools.primestream import PrimeStream


""" https://projecteuler.net/problem=3 """


class Solution:
    @staticmethod
    def iterative():
        num = 600851475143
        sqrt_num = int(num**(1/2))+1
        stream = PrimeStream.prime_stream(sqrt_num)

        i = next(stream)
        lpf = -1
        while i <= num:
            if num % i == 0:
                lpf = i
                while num % i == 0:
                    num //= i
            i = next(stream)
        return lpf


if __name__ == "__main__":
    Compete.estimate_method(Solution.iterative)
    print(f"\nAnswer: {Solution.iterative()}")
