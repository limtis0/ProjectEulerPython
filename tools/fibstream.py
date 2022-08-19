import collections


class FibStream:
    @staticmethod
    def fib_stream() -> collections.Iterator:
        yield 1
        yield 2
        a, b = 1, 2
        while True:
            a, b = b, a + b
            yield a
