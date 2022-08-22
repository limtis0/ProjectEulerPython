from tools.compete import Compete


''' https://projecteuler.net/problem=28 '''


class Solution:
    @staticmethod
    def solution():
        s = 1
        cur_num = 1
        for i in range(2, 1001 + 1, 2):
            for _ in range(4):
                cur_num += i
                s += cur_num
        return s


if __name__ == '__main__':
    Compete.estimate_method(Solution.solution)
    print(f'\nAnswer: {Solution.solution()}')
