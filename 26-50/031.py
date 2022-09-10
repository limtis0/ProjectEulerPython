from tools.compete import Compete

''' https://projecteuler.net/problem=26 '''


class Solution:
    PENCE = (1, 2, 5, 10, 20, 50, 100, 200)

    @staticmethod
    def dp(amount):
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in Solution.PENCE:
            for i in range(1, amount+1):
                if i - coin >= 0:
                    dp[i] += dp[i-coin]
        return dp[-1]


if __name__ == '__main__':
    Compete.estimate_method(Solution.dp, 200, repeat=1000)
    print(f'\nAnswer: {Solution.dp(200)}')
