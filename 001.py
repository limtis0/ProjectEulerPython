from tools.compete import Compete


''' https://projecteuler.net/problem=1 '''


class Solution:
    @staticmethod
    def bruteforce():
        s = 0
        for i in range(3, 1000):
            if i % 3 == 0 or i % 5 == 0:
                s += i
        return s

    @staticmethod
    def oneliner_bruteforce():
        return sum([i for i in range(3, 1000) if not (i % 3 and i % 5)])

    @staticmethod
    def sets():
        s = 0
        for i in set(range(3, 1000, 3)).union(set(range(5, 1000, 5))):
            s += i
        return s

    @staticmethod
    def oneliner_sets():
        return sum(set(range(3, 1000, 3)).union(set(range(5, 1000, 5))))


if __name__ == '__main__':
    Compete.compare_methods(Solution, repeat=100)
    print(f'\nAnswer: {Solution.oneliner_sets()}')
