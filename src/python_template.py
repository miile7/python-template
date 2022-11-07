from argparse import ArgumentParser
from version import get_version
from typing import TypedDict
from typing_extensions import Unpack


NAME = "python-template"


class ParserArgs(TypedDict):
    pass


def get_arg_parser() -> ArgumentParser:
    parser = ArgumentParser(prog=NAME)

    parser.add_argument(
        "--version", "-V", action="version", version=f"{NAME}, version {get_version()}"
    )

    return parser


def main(**kwargs: Unpack[ParserArgs]) -> None:
    parser = get_arg_parser()
    args = parser.parse_args(kwargs if len(kwargs) > 0 else None)


if __name__ == '__main__':
    main()
