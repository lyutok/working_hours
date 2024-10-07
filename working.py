import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if matches := re.search(r"^([0-9][0-9]?):?([0-5][0-9])? (AM|PM) to ([0-9][0-9]?):?([0-5][0-9])? (AM|PM)$", s):
        hours1 = matches.group(1)
        min1 = matches.group(2)
        part1 = matches.group(3)

        hours2 = matches.group(4)
        min2 = matches.group(5)
        part2 = matches.group(6)


        if min1 is None and min2 is None:
            return f"{time(hours1, part1):02}:00 to {time(hours2, part2):02}:00"
        elif min1 is None:
            return f"{time(hours1, part1):02}:00 to {time(hours2, part2):02}:{min2}"
        elif min2 is None:
            return f"{time(hours1, part1):02}:{min1} to {time(hours2, part2):02}:00"
        else:
            return f"{time(hours1, part1):02}:{min1} to {time(hours2, part2):02}:{min2}"

    else:
        raise ValueError
        # sys.exit(ValueError)


def time(h, am_pm):
    if am_pm == "AM":
        if 0 < int(h) < 12:
            return int(h)
        elif int(h) == 12:
            return 0
    elif am_pm == "PM":
        if 0 < int(h) < 12:
            return int(h) + 12
        elif int(h) == 12:
            return int(h)


if __name__ == "__main__":
    main()
