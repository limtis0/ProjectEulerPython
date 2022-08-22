from tools.compete import Compete
from itertools import permutations


''' https://projecteuler.net/problem=24 '''


class Solution:
    @staticmethod
    def itertools():
        return ''.join(list(permutations('0123456789'))[999999])

    @staticmethod
    def factorial_ns():
        thresh = 999999
        res = ''

        nums = [i for i in range(9+1)]
        facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

        for i in range(len(nums)-1, -1, -1):
            index, thresh = divmod(thresh, facts[i])
            res += str(nums.pop(index))

        return res


if __name__ == '__main__':
    Compete.compare_methods(Solution, repeat=10)
    print(f'\nAnswer: {Solution.factorial_ns()}')
