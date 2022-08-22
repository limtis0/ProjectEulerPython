from tools.compete import Compete
from enum import IntEnum


''' https://projecteuler.net/problem=19 '''


class Week(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class Month(IntEnum):
    JANUARY = 0
    FEBRUARY = 1
    MARCH = 2
    APRIL = 3
    MAY = 4
    JUNE = 5
    JULY = 6
    AUGUST = 7
    SEPTEMBER = 8
    OCTOBER = 9
    NOVEMBER = 10
    DECEMBER = 11


class Solution:
    @staticmethod
    def _is_leap_year(year):
        return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

    @staticmethod
    def _month_days_count(month, year):
        if month in (Month.SEPTEMBER, Month.APRIL, Month.JUNE, Month.NOVEMBER):
            return 30
        elif month == Month.FEBRUARY:
            return 29 if Solution._is_leap_year(year) else 28
        return 31

    @staticmethod
    def _add_month_to_day(day, month, year):
        return (day + Solution._month_days_count(month, year)) % 7

    @staticmethod
    def solution():
        curDay = Week.TUESDAY  # Jan 1901 was Tuesday
        sum_sundays = 0
        for year in range(1901, 2000+1):
            for month in Month:
                curDay = Solution._add_month_to_day(curDay, month, year)
                if curDay == Week.SUNDAY:
                    sum_sundays += 1
        return sum_sundays


if __name__ == '__main__':
    Compete.estimate_method(Solution.solution)
    print(f'\nAnswer: {Solution.solution()}')
