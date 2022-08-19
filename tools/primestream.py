import collections

from bitarray import bitarray


class PrimeStream:
    @staticmethod
    def prime_stream(cap: int) -> collections.Iterator:
        cap = int(cap)
        cap_sqrt = int(cap ** 0.5)

        primes = bitarray(cap)
        primes.setall(1)
        primes[0] = primes[1] = False
        primes[2] = True

        yield 2
        for i in range(3, cap_sqrt+1, 2):
            if primes[i]:
                yield i
                primes[i*i::i] = False

        cap_sqrt += 1 if cap_sqrt % 2 == 0 else 2
        for i in range(cap_sqrt, cap, 2):
            if primes[i]:
                yield i
