#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program will print all muliplication table 0-9


def main():
    # This program will print all muliplication table 0-9
    # process & output
    for counter1 in range(0, 10):
        for counter2 in range(0, 13):
            total = counter1 * counter2
            print("{0} x {1} = {2}".format(counter1, counter2, total))

    print("\nDone.")


if __name__ == "__main__":
    main()
