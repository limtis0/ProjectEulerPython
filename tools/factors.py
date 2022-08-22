import collections


class Factors:
    @staticmethod
    def factors(num: int) -> collections.Iterator:
        if num < 1:
            return

        sqrt = int(num ** (1 / 2))
        for i in range(1, sqrt + 1):
            if num % i == 0:
                yield i
                div_2 = num // i
                if div_2 != i:
                    yield div_2

    @staticmethod
    def count_factors(num: int) -> int:
        return sum(1 for _ in Factors.factors(num))

    @staticmethod
    def sum_factors(num: int) -> int:
        return sum(i for i in Factors.factors(num))
