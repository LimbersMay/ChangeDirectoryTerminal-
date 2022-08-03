#!/usr/bin/python

import argparse
from pathlib import Path

def cli() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        prog='change-dir',
        description='Change directory to the specified path.',
    )

    parser.add_argument(
        '--path-to-dir',
        type=Path,
        help='Path to change to.',
    )

    parser.add_argument(
        '-n', '--name',
        type=str,
        help='Name of the path to register.'
    )

    parser.add_argument(
        '-p', '--path',
        type=Path,
        help='Path to register.'
    )

    parser.add_argument(
        '-l', '--list',
        default=False,
        action='store_true',
        help='List all registered paths.'
    )

    return parser.parse_args()

import os
if __name__ == '__main__':
    # os.chdir("/home/limbers/Documents")
    # os.system("pwd")
    # os.system("/usr/bin/zsh")

    args = cli()

    print(args.name)
    print(args.path)