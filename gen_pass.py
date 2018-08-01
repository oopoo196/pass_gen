#!/usr/bin/env python3

import argparse
import random


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--length",
        type=int,
        help="The password length"
    )
    parser.add_argument(
        "-c", "--count",
        type=int,
        help="The number of passwords to generate"
    )
    parser.add_argument(
        "-s", "--special",
        help="Is there a need to use special characters",
        action="store_true"
    )
    return parser.parse_args()


def gen_pass(length, is_use_special_symbols=False):
    symbols = "qwertyuiopasdfghjklzxcvbnm" \
              "QWERTYUIOPASDFGHJKLZXCVBNM" \
              "1234567890"
    if is_use_special_symbols:
        symbols += "~!@#$%^&*()+`'\";:<>/\|"
    return "".join([random.choice(symbols) for j in range(length)])


if __name__ == "__main__":
    args = parse_args()

    pass_len = min(args.length or 18, 100)
    count = min(args.count or 1, 15)
    is_spec_symbols = args.special

    for i in range(count):
        print(gen_pass(pass_len, is_spec_symbols))
