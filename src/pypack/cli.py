# -*- coding: utf-8 -*-

"""Console script for pypack."""
import argparse

from pypack import __version__


def get_parser():
    """Defines options for pypack."""
    parser = argparse.ArgumentParser(
        prog="pypack",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=__doc__,
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="be more verbose")
    parser.add_argument(
        "-V", "--version", action="version", version="%(prog)s {}".format(__version__)
    )
    # Add more arguments as needed here

    return parser


def main(args=None):
    """Console script for pypack."""
    parser = get_parser()
    args = parser.parse_args(args)

    # Process args here
    print("Replace this message by putting your code into " "pypack.cli.main")
    print("See argparse tutorial at https://docs.python.org/3/howto/argparse.html")


if __name__ == "__main__":
    main()  # pragma: no cover
