#!/bin/python3

import csv
from random import seed, randrange


# Shakespearean insult generator
def insult():
    with open("shakespeare_list.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",")
        seed()
        row_count = sum(1 for row in spamreader)
        x = randrange(1, row_count)
        y = randrange(1, row_count)
        z = randrange(1, row_count)
        a = ""
        b = ""
        c = ""

        csvfile.seek(0)
        for index, row in enumerate(spamreader):
            if index == x:
                a = row[0]
            elif index == y:
                b = row[1]
            elif index == z:
                c = row[2]
        print(f"Thou {a} {b} {c}!")


def main():
    insult()


if __name__ == "__main__":
    main()
