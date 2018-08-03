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
        "-n", "--number",
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
    for j in range(length):
        print(
            random.choice(
                "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
                + ("~!@#$%^&*()+;:<>/\|" if is_use_special_symbols else "")
            ),
            end="\n" if j == length - 1 else ""
        )


if __name__ == "__main__":
    args = parse_args()

    for i in range(args.number or 1):
        gen_pass(args.length or 20, args.special)
