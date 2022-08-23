from pathlib import Path
from copy import deepcopy


class Triangle:
    def __init__(self, data):
        if not self.is_triangular(len(data)):
            raise Exception(f'List is not triangular, length={len(data)}')

        self._triangle = []
        data = deepcopy(data)

        size = 1
        while size <= len(data):
            self._triangle.append(data[:size])
            del data[:size]
            size += 1

    @classmethod
    def from_file(cls, file: Path):
        with open(file, 'r') as text:
            data = []
            for num in text.read().split():
                data.append(int(num))
            return cls(data)

    def get_list(self):
        return deepcopy(self._triangle)

    @staticmethod
    def is_triangular(num):
        if num < 0:
            return False

        # Equation is n*(n+1)/2 == num
        # n^2 + n = 2*num
        # n^2 + n - 2*num = 0
        # With quadratic formula:
        # a, b = 1, 1
        c = -2 * num
        d = 1 - 4 * c

        if d < 0:
            return False

        sqrt_d = d**(1/2)
        root1 = (-1 + sqrt_d) / 2
        root2 = (-1 - sqrt_d) / 2

        if (root1 > 0 and root1.is_integer()) or (root2 > 0 and root2.is_integer()):
            return True

        return False
