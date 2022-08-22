from tools.compete import Compete
from tools.factors import Factors


''' https://projecteuler.net/problem=12 '''


class Solution:
    @staticmethod
    def naive():
        i, n = 1, 1
        while Factors.count_factors(n) < 500:
            i += 1
            n += i
        return n

    '''
    As Nth and N+1th triangle numbers have no factors in common, you can count number of factors for the Nth number
    as [fact(n/2) * fact(n+1)]
    or [fact(n) * fact((n+1)/2)].
    Triangular(N) == n*(n+1)//2, it can be seen here, probably.
    '''
    @staticmethod
    def smart():
        cnt = n = 0
        while cnt < 500:
            n += 1
            if n % 2 == 0:
                cnt = Factors.count_factors(n//2) * Factors.count_factors(n+1)
            else:
                cnt = Factors.count_factors(n) * Factors.count_factors((n+1)//2)
        return n*(n+1)//2


if __name__ == '__main__':
    Compete.compare_methods(Solution, repeat=3)
    print(f'\nAnswer: {Solution.smart()}')
