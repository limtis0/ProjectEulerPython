from tools.compete import Compete


""" https://projecteuler.net/problem=9 """


class Solution:
    @staticmethod
    def bruteforce():
        for c in range(997, 2, -1):
            for b in range(c // 2, 1001-c):
                if b + c >= 1000:
                    break
                a = 1000 - b - c
                if a*a + b*b == c*c:
                    return a*b*c


if __name__ == "__main__":
    Compete.estimate_method(Solution.bruteforce)
    print(f"\nAnswer: {Solution.bruteforce()}")
