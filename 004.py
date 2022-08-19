from tools.compete import Compete


""" https://projecteuler.net/problem=4 """


class Solution:
    @staticmethod
    def _is_palindrome(num):
        return str(num) == str(num)[::-1]

    @staticmethod
    def bruteforce():
        mn = 0
        for n1 in range(999, 99, -1):
            for n2 in range(999, 99, -1):
                multi = n1 * n2
                if Solution._is_palindrome(multi):
                    mn = max(mn, multi)
        return mn

    @staticmethod
    def bruteforce_div11():
        mn = 0
        for n1 in range(999, 99, -1):
            # One of the numbers must be divisible by 11, because ABCCBA = 11(9091a + 910b + 100c)
            for n2 in range(990, 120, -11):
                multi = n1 * n2
                if Solution._is_palindrome(multi):
                    mn = max(mn, multi)
        return mn


if __name__ == "__main__":
    Compete.compare_methods(Solution, repeat=5)
    print(f"\nAnswer: {Solution.bruteforce_div11()}")
