#!/usr/bin/python
import os
import argparse
import sys
from pathlib import Path
from helpers.fichero import Fichero


def changeDirectory(fichero: Fichero, path: str):
    # If we received the path

    # Check if the path exists in our list of paths
    try:
        path = fichero.obtener_valor(path_to_dir)
        os.chdir(path)
        os.system("usr/bin/zsh")

        return

    except KeyError:
        pass

    if not Path(path).exists():
        print(f"{path} does not exist.")
        return

    os.chdir(path_to_dir)
    os.system("/usr/bin/zsh")


    
def process_args(path_to_dir: Path, name: str, path: str):

    fichero = Fichero('config/directories.json')

    if path_to_dir:
        changeDirectory(fichero, path_to_dir)
        return

    print(name, path)
    


def cli() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        prog='change-dir',
        description='Change directory to the specified path.',
    )

    parser.add_argument(
        '-c', '--change',
        type=str,
        help='Path to change to.',
    )

    parser.add_argument(
        '-n', '--name',
        type=str,
        help='Name of the path to register.'
    )

    parser.add_argument(
        '-p', '--path',
        type=str,
        help='Path to register.'
    )

    parser.add_argument(
        '-l', '--list',
        default=False,
        action='store_true',
        help='List all registered paths.'
    )

    return parser.parse_args()


if __name__ == '__main__':
    # os.chdir("/home/limbers/Documents")
    # os.system("pwd")
    # os.system("/usr/bin/zsh")

    args = cli()

    process_args(args.change, args.name, args.path)
