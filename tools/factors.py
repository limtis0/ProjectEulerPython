import collections


class Factors:
    std = {1: [1], 2: [1, 2], 3: [1, 3]}

    @staticmethod
    def factors(num: int) -> collections.Iterator:
        if num < 1:
            return

        if num in Factors.std.keys():
            for i in Factors.std[num]:
                yield i
            return
        i = 1
        sqrt = int(num ** (1 / 2))
        while i < sqrt:
            if num % i == 0:
                yield i
                yield num // i
            i += 1
        if num % sqrt == 0:
            yield sqrt

    @staticmethod
    def count_factors(num: int) -> int:
        return sum(1 for _ in Factors.factors(num))

    @staticmethod
    def sum_factors(num: int) -> int:
        return sum(i for i in Factors.factors(num))
