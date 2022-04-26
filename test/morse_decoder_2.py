# wabun morse decoder
# 2022/4/26
# IYN elec.

import sys

test_dat = [
    3, 93, 0,
    6, 51, "ヘ",
    9, 27, "゛",
    12, 21, "ラ",
    15, 18, "ヌ",
    0, 0, "5",
    0, 0, "4",
    0, 24, "ク",
    0, 0, "3",
    30, 39, "ウ",
    33, 36, "チ",
    0, 0, "ト",
    0, 0, "ミ",
    42, 48, "ノ",
    45, 0, "゜",
    0, 0, "?",
    0, 0, "2",
    54, 75, "イ",
    57, 66, "ナ",
    60, 63, "カ",
    0, 0, "オ",
    0, 0, "ヰ",
    69, 72, "ロ",
    0, 0, "ン",
    0, 0, "テ",
    78, 84, "ヤ",
    81, 186, "ツ",
    0, 0, "ヱ",
    87, 90, "ヲ",
    0, 0, "セ",
    0, 0, "1",
    96, 141, "ム",
    99, 120, "タ",
    102, 111, "ホ",
    105, 108, "ハ",
    0, 0, "6",
    0, 0, "メ",
    114, 117, "マ",
    0, 0, "モ",
    0, 0, "ユ",
    123, 132, "ワ",
    126, 129, "ニ",
    0, 0, "キ",
    0, 0, "サ",
    135, 138, "ケ",
    0, 0, "ル",
    0, 0, "エ",
    144, 165, "ヨ",
    147, 156, "リ",
    150, 153, "フ",
    0, 0, "7",
    0, 0, "ヒ",
    159, 162, "ネ",
    0, 0, "シ",
    0, 0, "ア",
    168, 177, "レ",
    171, 174, "ソ",
    0, 0, "8",
    0, 0, "ス",
    180, 183, "コ",
    0, 0, "9",
    0, 0, "0",
    0, 0, "ー",
]

def decoder(in_str):

    pointer = 0
    # trace tree
    for letter in in_str:

        if letter  == '.':
            pointer = test_dat[pointer]
        elif letter == '-':
            pointer = test_dat[pointer + 1]
        else:
            # illegal string
            pointer = 0
            break
        
        # error pattern detected
        if pointer == 0:
            break
    # --- for in_str

    if pointer == 0:
        out_str = 'error'
    else:
        out_str = test_dat[pointer + 2]

    return out_str


def main(argv):
    return decoder(argv)


if __name__ == '__main__':
    main(sys.argv[1:])

#eof
