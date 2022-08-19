from tools.compete import Compete


''' https://projecteuler.net/problem=2 '''


class Solution:
    @staticmethod
    def _recursion(n1=1, n2=2):
        if n1 + n2 > 4_000_000:
            return
        n3 = n1+n2
        if n3 % 2 == 0:
            yield n3
        yield from Solution._recursion(n1=n2, n2=n3)

    @staticmethod
    def recursive():
        return 2 + sum(Solution._recursion())

    @staticmethod
    def iterative():
        n1, n2 = 1, 2
        s = 0
        while n2 < 4_000_000:
            if n2 % 2 == 0:
                s += n2
            n1, n2 = n2, n1 + n2
        return s


if __name__ == '__main__':
    Compete.compare_methods(Solution, repeat=100)
    print(f'\nAnswer: {Solution.iterative()}')
