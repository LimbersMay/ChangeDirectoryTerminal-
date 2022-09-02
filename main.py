#!/usr/bin/python
import os
import argparse
import sys
from pathlib import Path
from helpers.fichero import Fichero

user_shell = os.environ['SHELL']

def switch_directory(fichero: Fichero, path: str):
    # If we received the path

    # Check if the path exists in our list of paths
    try:
        path = fichero.obtener_valor(path)
        os.chdir(path)
        os.system(user_shell)

        return

    except KeyError:
        pass

    if not Path(path).exists():
        print(f"{path} does not exist.")
        return

    os.chdir(path)
    os.system(user_shell)

def create_path_json(fichero: Fichero, name: str, path: str):

    # Check if the path exists
    if not Path(path).exists():
        print(f"{path} does not exist.")

        return

    fichero.guardar_valor(name, path)
    print(f"{name} registered as {path}")

def list_paths(fichero: Fichero):
    for key, value in fichero.listar_valores().items():
        print(f"{key} -> {value}")
    
def delete_path(fichero: Fichero, name: str):
    fichero.eliminar_valor(name)
    print(f"{name} deleted.")

def save_actual_path(fichero: Fichero):
    actual_path = os.getcwd()
    fichero.guardar_valor('last_path', actual_path)
    print(f"{actual_path} registered")

def move_to_last_path(fichero: Fichero):
    last_path = fichero.obtener_valor('last_path')

    os.chdir(last_path)
    os.system(user_shell)

def process_args(path_to_switch: str, name: str, path: str, list_register: bool, delete: str, register: bool, move: bool):

    fichero = Fichero(Path(__file__).parent / "config/directories.json")

    if path_to_switch:
        switch_directory(fichero, path_to_switch)

    if name and path:
        create_path_json(fichero, name, path)

    if list_register:
        list_paths(fichero)

    if delete:
        delete_path(fichero, delete)

    if register:
        save_actual_path(fichero)

    if move:
        move_to_last_path(fichero)
        

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

    parser.add_argument(
        '-r', '--register',
        default=False,
        action='store_true',
        help='Register the actual path'
    )

    parser.add_argument(
        '-m', '--move',
        default=False,
        action='store_true',
        help='Move to the last path registered'
    )

    return parser.parse_args()


if __name__ == '__main__':
    # os.chdir("/home/limbers/Documents")
    # os.system("pwd")
    # os.system("/usr/bin/zsh")

    args = cli()

    process_args(args.switch, args.name, args.path, args.list, args.delete, args.register, args.move)
