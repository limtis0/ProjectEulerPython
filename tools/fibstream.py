import collections


class FibStream:
    def __new__(cls):
        return FibStream.fib_stream()

    @staticmethod
    def fib_stream() -> collections.Iterator:
        yield 1
        yield 2
        a, b = 1, 2
        while True:
            a, b = b, a + b
            yield a
