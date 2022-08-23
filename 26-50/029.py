from tools.compete import Compete


''' https://projecteuler.net/problem=29 '''


class Solution:
    @staticmethod
    def oneliner():
        return len(set(i**j for i in range(2, 101) for j in range(2, 101)))


if __name__ == '__main__':
    Compete.estimate_method(Solution.oneliner)
    print(f'\nAnswer: {Solution.oneliner()}')
