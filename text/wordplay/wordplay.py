#!/bin/python3
from random import randrange, seed
import string
import sys

from nouns import nouns
from verbs import verbs
from prepositions import prepositions
from adj import adj
from pronouns import pronouns

# Program to use wordplay from people's sentences

# shared variables
seed()


# random_caps
# {{{
def random_caps(text):
    new_string = ""
    for i in range(len(text)):
        a = randrange(1, 10)
        b = text[i]
        if a > 5:
            new_string += b.upper()
        elif a < 5:
            new_string += b.lower()
        else:
            new_string += b
    print(new_string.rstrip("\n"))


# }}}
# sentence_reverse
# {{{
def sentence_reverse(text):
    print(text.rstrip("\n")[::-1])


# }}}
# flip_punct
# {{{
def flip_punct(text):
    new_string = ""
    for i in range(len(text)):
        b = text[i]
        if b.isupper():
            new_string += b.lower()
        elif b.islower():
            new_string += b.upper()
        else:
            new_string += b
    print(new_string.rstrip("\n"))


# }}}
# cap_all_words
# {{{
def cap_all_words(text):
    new_string = ""
    for item in text.split():
        new_string += item.capitalize() + " "
    print(new_string.rstrip("\n"))


# }}}
# random_words
# {{{
def random_words():
    v = randrange(0, len(pronouns))
    w = randrange(0, len(adj))
    ww = randrange(0, len(adj))
    x = randrange(0, len(nouns))
    y = randrange(0, len(verbs))
    z = randrange(0, len(prepositions))
    output = f"{pronouns[v].capitalize()} {verbs[y]} {prepositions[z]} {adj[w]} {adj[ww]} {nouns[x]}."
    print(output)


# }}}


def main():
    # need to do - accept input stream
    if sys.stdin.isatty():
        random_words()
    else:
        f = sys.stdin.read()
        x = randrange(0, 4)
        match x:
            case 0:
                random_caps(f)
            case 1:
                sentence_reverse(f)
            case 2:
                flip_punct(f)
            case 3:
                cap_all_words(f)


if __name__ == "__main__":
    main()
