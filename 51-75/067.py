from tools.compete import Compete
from tools.triangles import Triangle
from pathlib import Path
from copy import deepcopy


class Solution:
    triangle = Triangle.from_file(Path('067.txt')).get_list()

    @staticmethod
    def from_bottom():
        triangle = deepcopy(Solution.triangle)
        for row in range(len(triangle)-2, 0-1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += max(triangle[row+1][col], triangle[row+1][col+1])
        return triangle[0][0]


if __name__ == '__main__':
    Compete.estimate_method(Solution.from_bottom, repeat=20)
    print(f'\nAnswer: {Solution.from_bottom()}')
