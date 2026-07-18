#!/bin/python3

# quotes reading script
import csv
from random import seed, randrange

with open("quotes.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=";")
    seed()
    x = randrange(1, 75967)
    for index, row in enumerate(spamreader):
        if index == x:
            print(row[0])
