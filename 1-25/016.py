from tools.compete import Compete


''' https://projecteuler.net/problem=16 '''


class Solution:
    @staticmethod
    def oneliner():
        return sum(int(i) for i in str(2**1000))

    @staticmethod
    def oneliner_two():  # Two times faster
        return sum(map(int, str(2 ** 1000)))


if __name__ == '__main__':
    Compete.compare_methods(Solution, repeat=1000)
    print(f'\nAnswer: {Solution.oneliner_two()}')
