from argparse import ArgumentParser
from version import get_version
from typing import TypedDict
from typing_extensions import Unpack


NAME = "python-template"


class ParserArgs(TypedDict):
    pass


def print_version() -> None:
    print(f"{NAME}, version {get_version()}")


def get_arg_parser() -> ArgumentParser:
    parser = ArgumentParser(prog=NAME)

    parser.add_argument("--version", "-V", action=print_version)

    return parser


def main(**kwargs: Unpack[ParserArgs]) -> None:
    parser = get_arg_parser()
    args = parser.parse_args(kwargs if len(kwargs) > 0 else None)


if __name__ == '__main__':
    main()
