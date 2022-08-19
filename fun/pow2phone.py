from colorama import init, Fore, Style

"""
Trying to find a part of pi that has my phone number (*** *** ***) in it :)

For me, the answer is 2^89293
"""


def find_my_phone(phone: str) -> int:
    n, p = 2, 1
    while phone not in str(n) and p <= 500_000:
        n *= 2
        p += 1
    return p if p < 500_000 else -1


def print_my_phone(phone: str, power: int) -> None:
    powered = str(2**power)
    splitted = powered.split(phone)

    init(convert=True)
    blue = Fore.LIGHTBLUE_EX
    clear = Style.RESET_ALL
    print(f"{blue}Index: {powered.index(phone)}{clear}\n")
    print(f"{blue}2^{power}{clear} = {splitted[0]} {blue}{phone}{clear} {splitted[1]}")


if __name__ == "__main__":
    print_my_phone("MY PHONE NUMBER", 89293)
