#!/bin/python3

# color changing program // rgb, hex, hsl, cmyk
import argparse
import sys
import string


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rgb", help="rgb", action="store_true")
    parser.add_argument("-x", "--hex", help="hex", action="store_true")
    parser.add_argument("-s", "--hsl", help="hsl", action="store_true")
    parser.add_argument("-y", "--cmyk", help="cmyk", action="store_true")

    args = parser.parse_args()
    if len(sys.argv) - 1 == 1:  # excludes the script name
        pass
    else:
        raise Exception("One command please")  # more than one command entered
    if args.rgb:
        rgb_main(None)  # rgb_main expects some sort of input
    elif args.hex:
        rgb_main(hex_2_rgb())
    elif args.hsl:
        rgb_main(hsl_2_rgb())
    elif args.cmyk:
        rgb_main(cmyk_2_rgb())


# main rgb func where bulk of data is calculated // done
# {{{
def rgb_main(rgb_input):
    print(
        "\n***Disclaimer: rgb output to CMYK from CMYK input may differ because RGB has a larger color gamut than CMYK does***\n"
    )
    rgb_values = []
    hex_out = None
    hsl_out = None
    cmyk_out = None

    if rgb_input is None:
        pass
    else:
        rgb_values = rgb_input

    if rgb_input is None:  # meaning '-r' flag was pass
        while True:
            min_val = 0
            max_val = 255
            try:
                r = int(input("R value: "))
                g = int(input("G value: "))
                b = int(input("B value: "))

                x = min_val <= r and r <= max_val
                y = min_val <= g and g <= max_val
                z = min_val <= b and b <= max_val

                if all([x, y, z]):
                    rgb_values.extend([r, g, b])
                    break
                else:
                    print("Values must be between 0 && 255")
            except ValueError:
                print("Only integers")
        # calls functions from rgb values
        hex_out = rgb_2_hex(rgb_values)
        hsl_out = rgb_2_hsl(rgb_values)
        cmyk_out = rgb_2_cmyk(rgb_values)

    # if args are anything other than 'rgb'
    else:
        rgb_values = rgb_input
        hex_out = rgb_2_hex(rgb_values)
        hsl_out = rgb_2_hsl(rgb_values)
        cmyk_out = rgb_2_cmyk(rgb_values)

    print(
        f"RGB:\t\t{rgb_values}\nHex:\t\t{hex_out}\nHSL:\t\t{hsl_out}\nCMYK:\t\t{cmyk_out}"
    )


# }}}
# rgb 2 hex func // done
# {{{
def rgb_2_hex(rgb_values):
    new_string = "#"
    # not sure of better way to 'shorten' this block
    hex_chars = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]
    for item in rgb_values:
        output = divmod(item, 16)  # divmod calculates (floor(quotient), remainder)
        left = output[0]
        l_val = None
        if left > 9:  # if hex char is needed
            l_val = hex_chars[left]
        right = output[1]
        r_val = None
        if output[1] > 9:  # if hex char is needed
            r_val = hex_chars[right]
        if all([l_val, r_val]):  # if letters, not numbers essentially
            new_string += l_val + r_val
        elif l_val:
            new_string += l_val + str(right)
        elif r_val:
            new_string += str(left) + r_val
        else:
            new_string += str(left) + str(right)
    return new_string  # returns string '#xxxxxx'


# }}}
# rgb 2 hsl func // done
# {{{
def rgb_2_hsl(rgb_values):
    rgb_deltas = []
    for item in rgb_values:
        rgb_deltas.append(item / 255)  # changes rgb values to 0...1
    hue = None
    hue_degrees = 60  # used because HSL diagram is a circle
    saturation = None
    light = None
    output = None
    # hue calc
    cmax = max(rgb_deltas)
    cmin = min(rgb_deltas)
    total_delta = cmax - cmin

    if total_delta == 0:
        hue = 0
    # functions differ when r'g'b' values have max
    elif cmax == rgb_deltas[0]:
        hue = hue_degrees * (((rgb_deltas[1] - rgb_deltas[2]) / total_delta) % 6)
    elif cmax == rgb_deltas[1]:
        hue = hue_degrees * (((rgb_deltas[2] - rgb_deltas[0]) / total_delta) + 2)
    elif cmax == rgb_deltas[2]:
        hue = hue_degrees * (((rgb_deltas[0] - rgb_deltas[1]) / total_delta) + 4)
    # light calc
    light = (cmax + cmin) / 2
    light_fixed = 100 * light  # need it to be a percentage
    # saturation calc
    if total_delta == 0:
        saturation = 0
    else:
        saturation = total_delta / (1 - abs(2 * light - 1))  # eq. for saturation
        saturation *= 100  # need it to be a percentage
    output = [round(hue), round(saturation, 1), round(light_fixed, 1)]
    return output  # returns round nums, h is whole and s/l_f are .1 precision


# }}}
# rgb 2 cmyk func // done
# {{{
def rgb_2_cmyk(rgb_values):
    rgb_deltas = []
    output = None
    for item in rgb_values:
        rgb_deltas.append(item / 255)  # rgb values adjusted to 0...1
    k = 1 - max(rgb_deltas)
    c = (1 - rgb_deltas[0] - k) / (1 - k)
    m = (1 - rgb_deltas[1] - k) / (1 - k)
    y = (1 - rgb_deltas[2] - k) / (1 - k)
    output = [round(x * 100) for x in (c, m, y, k)]
    return output  # returns rounded ouput * 100 for percentages


# }}}
# hex 2 rgb func // done
# {{{
def hex_2_rgb():
    hex_input = None
    rgb_values = []
    ascii_values = string.ascii_letters + string.digits  # check for special chars
    hex_chars = ["a", "b", "c", "d", "e", "f"]
    while True:
        try:
            tmp_input = input("Please input hex color code: ")
            if len(tmp_input) != 6:
                continue
            if not all([x for x in tmp_input if x in ascii_values]):
                continue
            hex_input = list(tmp_input)
            break
        except ValueError:
            print("Please input correct values")
    # get value back by 16^1 and 16^0
    # #ffffff -> 255, 255, 255
    # each two letter sub group is R,G,B -> ff | ff | ff
    # left digit is * 16^1
    for i in range(0, len(hex_input), 2):
        a = hex_input[i]
        b = hex_input[i + 1]
        if a in hex_chars:
            a = 10 + hex_chars.index(a)
        else:
            a = int(a)
        if b in hex_chars:
            b = 10 + hex_chars.index(b)
        else:
            b = int(b)
        a *= 16
        rgb_values.append(a + b)
    return rgb_values  # return list [r, g, b[


# }}}
# hsl 2 rgb func // done
# {{{
def hsl_2_rgb():
    rgb_values = []
    rgb_deltas = []
    hsl_values = []
    while True:
        try:
            h = int(input("H: "))
            s = int(input("S: "))
            l = int(input("L: "))
            for item in (h, s, l):
                if h > 359 or h < 0:
                    continue
                elif s < 0 or s > 100:
                    continue
                elif l < 0 or l > 100:
                    continue
                else:
                    hsl_values.extend([h, s, l])
            break
        except ValueError:
            # reminder txt; h < 360 or else cause weird values
            print("0 <= h < 360, 0 < s//l < 100")
    s /= 100  # percentage normalize 0..1
    l /= 100
    # C, X, m are vars for hsl conversion
    C = (1 - (abs(2 * l - 1))) * s
    X = C * (1 - (abs(h / 60) % 2 - 1))
    m = l - (C / 2)
    # actual formulas to decide rgb
    if h >= 0 and h < 60:
        rgb_deltas.extend([C, X, 0])
    elif h >= 60 and h < 120:
        rgb_deltas.extend([X, C, 0])
    elif h >= 120 and h < 180:
        rgb_deltas.extend([0, C, X])
    elif h >= 180 and h < 240:
        rgb_deltas.extend([0, X, C])
    elif h >= 240 and h < 300:
        rgb_deltas.extend([X, 0, C])
    elif h >= 300 and h < 360:
        rgb_deltas.extend([C, 0, X])
    r = round((rgb_deltas[0] + m) * 255)
    g = round((rgb_deltas[1] + m) * 255)
    b = round((rgb_deltas[2] + m) * 255)
    rgb_values.extend([r, g, b])

    return rgb_values  # will return list [r, g, b]


# }}}
# cmyk to rgb func // done
# {{{
def cmyk_2_rgb():
    rgb_values = []
    cmyk_values = []
    while True:
        try:
            c = int(input("C: "))
            m = int(input("M: "))
            y = int(input("Y: "))
            k = int(input("K: "))
            for item in (c, m, y, k):
                if item <= 100 and item >= 0:
                    cmyk_values.extend([item])
                else:
                    continue
            break
        except ValueError:
            print("Please only include floats")
    tmp_list = [x / 100 for x in cmyk_values]  # cmyk are in %, normalize 0..1
    # round instead of int(), int truncates
    r = round(255 * (1 - tmp_list[0]) * (1 - tmp_list[3]))
    g = round(255 * (1 - tmp_list[1]) * (1 - tmp_list[3]))
    b = round(255 * (1 - tmp_list[2]) * (1 - tmp_list[3]))
    rgb_values.extend([r, g, b])

    return rgb_values  # will return a list of rgb [r, g, b]


# }}}

if __name__ == "__main__":
    main()
