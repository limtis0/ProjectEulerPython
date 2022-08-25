from tools.compete import Compete


''' https://projecteuler.net/problem=30 '''


class Solution:
    @staticmethod
    def solution():
        return sum(i for i in range(10, 9**5*5+1) if sum(int(c)**5 for c in str(i)) == i)


if __name__ == '__main__':
    Compete.estimate_method(Solution.solution, repeat=3)
    print(f'\nAnswer: {Solution.solution()}')
