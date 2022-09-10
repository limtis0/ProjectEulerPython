from tools.compete import Compete
from tools.palindromes import PalindromeStream, is_palindrome


''' https://projecteuler.net/problem=36 '''


class Solution:
    @staticmethod
    def solution():
        s = 0
        stream = PalindromeStream(1_000_000)
        for i in stream:
            if is_palindrome(i) and is_palindrome(bin(i)[2:]):
                s += i
        return s


if __name__ == '__main__':
    Compete.estimate_method(Solution.solution)
    print(f'\nAnswer: {Solution.solution()}')
