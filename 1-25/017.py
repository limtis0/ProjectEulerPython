from tools.compete import Compete


''' https://projecteuler.net/problem=17 '''


nums = {
    1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,  # 1-9
    10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8,  # 10-19
    20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6,  # 20-100
    'hundred': 7, 'and': 3
}


class Solution:
    @staticmethod
    def _hashtable(n):
        if n == 1000:
            return len('onethousand')

        count = 0
        if n >= 100:
            count += nums[n // 100]
            count += nums['hundred']
            if n % 100 != 0:  # if it is just 'hundreds'
                count += nums['and']
            else:
                return count

        tens = n % 100
        if tens <= 20 or tens in nums:
            count += nums[tens]
            return count

        count += nums[tens - tens % 10]
        count += nums[tens % 10]
        return count

    @staticmethod
    def hashtable():
        return sum(Solution._hashtable(i) for i in range(1, 1001))


if __name__ == '__main__':
    Compete.estimate_method(Solution.hashtable)
    print(f'\nAnswer: {Solution.hashtable()}')
