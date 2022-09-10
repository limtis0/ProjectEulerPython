class PalindromeStream:
    def __new__(cls, cap: int):
        return cls.palindrome_stream(cap)

    ''' Note: Unordered '''
    @staticmethod
    def palindrome_stream(cap: int):
        if cap < 0:
            return

        yield 0
        for i in range(1, (cap // 100)+1):
            if i <= 9:
                yield i

            # Mirror
            s = str(i)
            mirrored = int(s + s[::-1])
            if mirrored <= cap:
                yield mirrored

            # Add number and mirror
            for j in range(0, 9+1):
                mirrored = int(s + str(j) + s[::-1])
                if mirrored <= cap:
                    yield mirrored


def is_palindrome(element: any):
    s = str(element)
    return s == s[::-1]
