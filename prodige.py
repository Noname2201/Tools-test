#!/usr/bin/env python3
"""Command line utility named prodige with many options."""

import argparse
import sys


def main(argv=None):
    parser = argparse.ArgumentParser(description="Prodige CLI tool")
    parser.add_argument(
        "args",
        nargs="*",
        help="positional arguments that will form the base message",
    )
    parser.add_argument(
        "-m",
        "--message",
        help="explicit message to output instead of positional args",
        default="",
    )
    parser.add_argument(
        "-r",
        "--repeat",
        type=int,
        default=1,
        help="number of times to repeat the output",
    )
    parser.add_argument(
        "--reverse",
        action="store_true",
        help="reverse the message before printing",
    )
    parser.add_argument(
        "--upper",
        action="store_true",
        help="convert the message to uppercase",
    )
    parser.add_argument(
        "--lower",
        action="store_true",
        help="convert the message to lowercase",
    )
    parser.add_argument(
        "--prefix",
        help="string to prepend to the message",
        default="",
    )
    parser.add_argument(
        "--suffix",
        help="string to append to the message",
        default="",
    )
    parser.add_argument(
        "--delimiter",
        default=" ",
        help="delimiter used to join positional arguments",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="prodige 1.0",
    )

    if argv is None:
        argv = sys.argv[1:]
    opts = parser.parse_args(argv)

    if opts.message:
        message = opts.message
    else:
        message = opts.delimiter.join(opts.args)

    if not message:
        print("Prodige: no input provided")
        return

    if opts.reverse:
        message = message[::-1]
    if opts.upper:
        message = message.upper()
    if opts.lower:
        message = message.lower()

    message = f"{opts.prefix}{message}{opts.suffix}"

    for _ in range(max(opts.repeat, 1)):
        print(message)


if __name__ == "__main__":
    main()
