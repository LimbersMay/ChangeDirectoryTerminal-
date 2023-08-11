#!/usr/bin/python
import argparse
import os
from pathlib import Path

from helpers.user_repository import UserRepository

user_shell = os.environ['SHELL']


def switch_directory(user_repository: UserRepository, path: str):
    # If we received the path

    # Check if the path exists in our list of paths
    try:
        path = user_repository.find_one(path)
        os.chdir(path)
        os.system(user_shell)

        return

    except KeyError:
        print(f"Error trying to find {path} in the list of paths.")

    if not Path(path).exists():
        print(f"{path} does not exist.")
        return

    os.chdir(path)
    os.system(user_shell)


def create_path_json(user_repository: UserRepository, name: str, path: str):
    # Check if the path exists
    if not Path(path).exists():
        print(f"{path} does not exist.")

        return

    absolute_path = os.path.abspath(path)

    user_repository.save(name, absolute_path)
    print(f"{name} registered as {absolute_path}")


def list_paths(user_repository: UserRepository):
    for key, value in user_repository.find_all().items():
        print(f"{key} -> {value}")


def delete_path(user_repository: UserRepository, name: str):
    user_repository.delete(name)
    print(f"{name} deleted.")


def save_actual_path(user_repository: UserRepository):
    actual_path = os.getcwd()
    user_repository.save('last_path', actual_path)
    print(f"{actual_path} registered")


def move_to_last_path(user_repository: UserRepository):
    last_path = user_repository.find_one('last_path')

    os.chdir(last_path)
    os.system(user_shell)


def process_args(path_to_switch: str, name: str, path: str, list_register: bool, delete: str, register: bool,
                 move: bool):

    user_repository = UserRepository(Path(__file__).parent / "config/directories.json")

    if path_to_switch:
        switch_directory(user_repository, path_to_switch)

    if name and path:
        create_path_json(user_repository, name, path)

    if list_register:
        list_paths(user_repository)

    if delete:
        delete_path(user_repository, delete)

    if register:
        save_actual_path(user_repository)

    if move:
        move_to_last_path(user_repository)


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
        '-n', '--alias',
        type=str,
        help='Alias of the path to register.'
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
        help='Register a path. Register the current path as last if no path is specified'
    )

    parser.add_argument(
        '-g', '--goto-last',
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
