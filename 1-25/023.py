from tools.compete import Compete
from tools.factors import Factors


''' https://projecteuler.net/problem=23 '''


class Solution:
    abundants = {i for i in range(1, 28123+1) if Factors.sum_factors(i) - i > i}

    @staticmethod
    def hashmap():
        s = 0
        for i in range(1, 28123+1):
            found_pair = False
            for j in Solution.abundants:
                if i - j in Solution.abundants:
                    found_pair = True
                    break
            if not found_pair:
                s += i
        return s


if __name__ == '__main__':
    Compete.compare_methods(Solution, repeat=3)
    print(f'\nAnswer: {Solution.hashmap()}')
