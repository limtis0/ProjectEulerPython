from tools.compete import Compete
from tools.factors import Factors


"""https://projecteuler.net/problem=21"""


class Solution:
    @staticmethod
    def hashmap():
        found = {}
        s = 0
        for i in range(2, 10_001):
            if i not in found:
                facts = Factors.sum_factors(i) - i
                if facts != i and facts <= 10_000:
                    facts_2 = Factors.sum_factors(facts) - facts
                    if facts_2 == i:
                        s += facts + i
                        found[facts] = facts_2
        return s


if __name__ == "__main__":
    Compete.estimate_method(Solution.hashmap, repeat=10)
    print(f"\nAnswer: {Solution.hashmap()}")
