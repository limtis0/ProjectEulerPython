from tools.compete import Compete


''' https://projecteuler.net/problem=22 '''


class Solution:
    with open('022_names.txt', 'r') as file:
        names = sorted(file.read().replace('\'', '').split(','))

    scores = {letter: score for score, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1)}

    @staticmethod
    def linear():
        s = 0
        for line, name in enumerate(Solution.names, start=1):
            s += line * sum(Solution.scores[char] for char in name)
        return s


if __name__ == '__main__':
    Compete.estimate_method(Solution.linear, repeat=10)
    print(f'\nAnswer: {Solution.linear()}')
