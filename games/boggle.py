#!/bin/python3
import random
import argparse
import sys

# my attempt at a boggle gameboards


# main
# {{{
def main():
    random.seed()  # need new seed, otherwise all boards the same
    skip_key = None  # specific spot in dicts where multi-letter entries reside
    dict_choice = None  # which dict to choose based on args
    board_size = None  # 4, 5, 6 for classic, big and super; respectively
    if "-c" in sys.argv:
        skip_key = 14
        board_size = 4
        dict_choice = boggle.items()
    elif "-b" in sys.argv:
        skip_key = 8
        board_size = 5
        dict_choice = bb.items()
    elif "-s" in sys.argv:
        skip_key = 12
        board_size = 6
        dict_choice = sb.items()
    new_list = []  # our list that is going to hold the random values
    for key, value in dict_choice:
        output = None
        x = random.randrange(0, 5)  # the len of each entry if dict.value is 6
        if key == skip_key:
            if key == 14 or key == 8:
                y = random.randrange(0, 1)  # 0 == single chars, 1 == double char
                z = random.randrange(0, 4)
                if y == 1:
                    output = value[1]
                else:
                    output = value[0][z]
            # needed because we are checking if key matches, even though does not matter for super
            elif key == 12:
                output = value[x]

        else:
            output = value[x]

        new_list.append(output)
    random.shuffle(new_list)  # handy random function to shuffle 'dice'
    fl = new_list  # I did not want to type new_list[x] for every fstring var
    # I am sure there is a better way to do this
    if board_size == 4:
        for i in range(0, board_size * board_size, board_size):
            new_string = f"{fl[i]:3}{fl[i+1]:3}{fl[i+2]:3}{fl[i+3]:3}"
            print(new_string)
    elif board_size == 5:
        for i in range(0, board_size * board_size, board_size):
            new_string = f"{fl[i]:3}{fl[i+1]:3}{fl[i+2]:3}{fl[i+3]:3}{fl[i+4]:3}"
            print(new_string)
    elif board_size == 6:
        for i in range(0, board_size * board_size, board_size):
            new_string = (
                f"{fl[i]:3}{fl[i+1]:3}{fl[i+2]:3}{fl[i+3]:3}{fl[i+4]:3}{fl[i+5]:3}"
            )
            print(new_string)


# }}}
# input args
# {{{
def input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", help="choose 4x4 board", action="store_true")
    parser.add_argument("-b", help="choose 5x5 board", action="store_true")
    parser.add_argument("-s", help="choose 6x6 board", action="store_true")

    args = parser.parse_args()
    return args


# }}}
# boggle_dict
# {{{
boggle = {
    0: "AAEEGH",
    1: "ABBJOO",
    2: "ACHOPS",
    3: "AFFKPS",
    4: "AOOTTW",
    5: "CIMTOU",
    6: "DEILRX",
    7: "DELRVY",
    8: "DISTTY",
    9: "EEEEEE",
    10: "EEIISS",
    11: "EHRTVW",
    12: "EINOSU",
    13: "ELRTTY",
    14: ["HIMNU", "QU"],
    15: "HLNNKZ",
}
# }}}
# bb_dict
# {{{
bb = {
    0: "AAAFRS",
    1: "AAEEEE",
    2: "AAFIRS",
    3: "ADENNN",
    4: "AEEEEM",
    5: "AEEGMU",
    6: "AEGMNN",
    7: "AFIRSY",
    8: ["BJKXZ", "QU"],
    9: "CCENST",
    10: "CEIILT",
    11: "CEILPT",
    12: "CEIPST",
    13: "DDHNOT",
    14: "DHHLOR",
    15: "DHLNOR",
    16: "DHLNOR",
    17: "EIIITT",
    18: "EMOTTT",
    19: "ENSSSU",
    20: "FIPRSY",
    21: "GORRVW",
    22: "IPRRRY",
    23: "NOOTUW",
    24: "OOOTTU",
}
# }}}
# sb_dict
# {{{
sb = {
    0: "AAAFRS",
    1: "AAEEEE",
    2: "AAEEOO",
    3: "AAFIRS",
    4: "ABDEIO",
    5: "ADENNN",
    6: "AEEEEM",
    7: "AEEGMU",
    8: "AEGMNN",
    9: "AEILMN",
    10: "AEINOU",
    11: "AFIRSY",
    12: ["An", "Er", "He", "In", "Qu", "Th"],
    13: "BBJKXZ",
    14: "CCENST",
    15: "CDDLNN",
    16: "CEIITT",
    17: "CEIPST",
    18: "CFGNUY",
    19: "DDHNOT",
    20: "DHHLOR",
    21: "DHHNOW",
    22: "DHLNOR",
    23: "EHILRS",
    24: "EIILST",
    25: "EILPST",
    26: "EIO###",
    27: "EMTTTO",
    28: "ENSSSU",
    29: "GORRVW",
    30: "HIRSTV",
    31: "HOPRST",
    32: "IPRSYY",
    33: "JKQuWXZ",
    34: "NOOTUW",
    35: "OOOTTU",
}
# }}}
if __name__ == "__main__":
    main()
