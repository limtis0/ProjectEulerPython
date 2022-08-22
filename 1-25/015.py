from tools.compete import Compete


''' https://projecteuler.net/problem=15 '''


class Solution:
    @staticmethod
    def graphs(N):
        N += 1  # N cells == N+1 vertices
        m = [[1 if 0 in (x, y) else 0 for x in range(N)] for y in range(N)]
        for y in range(1, N):
            for x in range(1, N):
                m[y][x] += m[y-1][x]
                m[y][x] += m[y][x-1]
        return m[N-1][N-1]


if __name__ == '__main__':
    Compete.estimate_method(Solution.graphs, 20, repeat=1000)
    print(f'\nAnswer: {Solution.graphs(20)}')

