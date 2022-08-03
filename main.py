#!/usr/bin/python
import os
import argparse
import sys
from pathlib import Path
from helpers.fichero import Fichero


def switchDirectory(fichero: Fichero, path: str):
    # If we received the path

    # Check if the path exists in our list of paths
    try:
        path = fichero.obtener_valor(path)
        os.chdir(path)
        os.system("/usr/bin/zsh")

        return

    except KeyError:
        pass

    if not Path(path).exists():
        print(f"{path} does not exist.")
        return

    os.chdir(path)
    os.system("/usr/bin/zsh")

def createDirectoryJson(fichero: Fichero, name: str, path: str):

    # Check if the path exists
    if not Path(path).exists():
        print(f"{path} does not exist.")

        return

    fichero.guardar_valor(name, path)
    print(f"{name} registered as {path}")

def listPaths(fichero: Fichero):
    for key, value in fichero.listar_valores().items():
        print(f"{key} -> {value}")
    
def deletePath(fichero: Fichero, name: str):
    fichero.eliminar_valor(name)
    print(f"{name} deleted.")

def process_args(path_to_switch: str, name: str, path: str, list_paths: bool, delete: str):

    fichero = Fichero(Path(__file__).parent / "config/directories.json")

    if path_to_switch:
        switchDirectory(fichero, path_to_switch)

    if name and path:
        createDirectoryJson(fichero, name, path)

    if list_paths:
        listPaths(fichero)

    if delete:
        deletePath(fichero, delete)
        

def cli() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        prog='change-dir',
        description='Change directory to the specified path.',
    )

    parser.add_argument(
        '-s', '--switch',
        type=str,
        help='Path to switch to.',
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
        '-d', '--delete',
        type=str,
        help='Name of the path to delete.'
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

    process_args(args.switch, args.name, args.path, args.list, args.delete)
